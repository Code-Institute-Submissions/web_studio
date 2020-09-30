import json
import os

import requests
import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST

from appointments.forms import AppointmentForm
from products.models import Product
from .forms import OrderForm
from .models import Order


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={

            'name': request.POST.get('name'),
            'email': request.POST.get('email'),

        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request, product_type):
    order_form = OrderForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'

    if product_type == 'blog':
        total = round(Product.objects.get(name='blog').price)
    elif product_type == 'website':
        total = round(Product.objects.get(name='website').price)
    elif product_type == 'online-store':
        total = round(Product.objects.get(name='online-store').price)
    elif product_type == 'consultation':
        total = round(Product.objects.get(name='consultation').price)
    else:
        # setting total to 1999 in case user is messing with urls
        total = 1999

    # stripe amount in cents
    stripe_total = total * 100

    stripe.api_key = stripe_secret_key
    # create intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY

    )

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'user': request.user.username,
        'type': product_type,
        'grand_total': total,

    }
    if request.method == 'POST':

        form_data = {
            'name': request.POST.get('name'),
            'street1': request.POST.get('street1'),
            'city': request.POST.get('city'),
            'post_code': request.POST.get('post_code'),
            'country': request.POST.get('country'),
            'email': request.POST.get('email'),
            'product_type': product_type,
            'grand_total': total,
        }
        # IF CUSTOMER IS PURCHASING EXTRA CONSULTATION
        # WE WILL STORE IT IN DATABASE
        if product_type == 'consultation':
            appointment_data = {
                'name': request.POST['name'],
                'email': request.POST['email'],
                'phone_num': request.POST['phone_num'],
                'password': 'user_password',
                'site_type': request.POST['site_type'],
                'time_slot': request.POST['time_slot'],
                'project': request.POST['project'],
                'done': 'done' in request.POST,
            }

            consultation_form = AppointmentForm(appointment_data)
            context = {
                'form': consultation_form
            }
            if consultation_form.is_valid():
                try:
                    """
                    IF FORM IS VALID, WE WILL SAVE IT TO DB 
                    """
                    consultation_form.save()

                    """
                    sending email to owner of the website, informing him about new appointment
                    using MAILGUN service as it's already running for globtopus.com
                    """
                    site_types = {
                        '1': 'blog', '2': 'website', '3': 'online store', '4': 'something else'
                    }
                    times = {
                        '1': '8am-12am', '2': '12am-4pm', '3': '4pm-8pm',
                    }

                    request_url = "https://api.eu.mailgun.net/v3/globtopus.com/messages"
                    key = os.getenv('MAILGUN_API_KEY')
                    recipient = 'marcelkolarcik@gmail.com'
                    requests.post(request_url, auth=('api', key), data={
                        'from': 'marcellidesigns marcelkolarcik@gmail.com',
                        'to': recipient,
                        'subject': 'New appointment',
                        "template": "marcellidesigns_appointment",
                        "h:X-Mailgun-Variables":
                            json.dumps(
                                {'welcome': 'New appointment : paid',
                                 'body_1': request.POST['email'] + ' - ' + request.POST['phone_num'] + ' - ' +
                                           request.POST[
                                               'name'],
                                 'body_2': request.POST['project'],
                                 'question': times[request.POST['time_slot']],
                                 'sign-in': 'Site',
                                 'welcome_team': 'Marcelli Designs', })
                    })

                    # sending email to customer, confirming new appointment
                    request_url = "https://api.eu.mailgun.net/v3/globtopus.com/messages"
                    key = os.getenv('MAILGUN_API_KEY')
                    recipient = request.POST['email']
                    requests.post(request_url, auth=('api', key), data={
                        'from': 'marcellidesigns marcelkolarcik@gmail.com',
                        'to': recipient,
                        'subject': 'Your appointment',
                        "template": "marcellidesigns_customer_appointment",
                        "h:X-Mailgun-Variables":
                            json.dumps(
                                {'welcome': 'Your appointment',
                                 'customer_name': request.POST['name'],
                                 'time': times[request.POST['time_slot']],
                                 'phone': request.POST['phone_num'],
                                 'project': request.POST['project'],
                                 'site_type': site_types[request.POST['site_type']],

                                 'welcome_team': 'Marcelli Designs', })
                    })


                except:
                    messages.error(request, 'There was an error with your form. \
                                                                        Please double check your information')

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # if order form is valid try to add order to DB

            try:
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.grand_total = total
                order.total = total
                order.product_type = product_type
                order.save()

                messages.success(request, 'Your order was created successfully ')

                return redirect(reverse('checkout_success', args=[order.order_number]))

            except:
                # else send notification to user, that something is wrong
                messages.error(request, 'There was an error with your form order form. \
                                               Please double check your information.')
                context['order_form'] = order_form





        else:
            # if form is not valid, send notification to user, that something is wrong
            messages.error(request, 'There was an error with your form \
                        Please double check your information.')
            context['order_form'] = order_form

    return render(request, template, context)


# Handle successful checkouts
def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'user': request.user.username,
    }

    return render(request, template, context)
