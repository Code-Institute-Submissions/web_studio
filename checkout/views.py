import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST

from appointments.models import Appointment
from products.models import Product
from projects.forms import ProjectForm
from .forms import OrderForm
from .models import Order

# ajax call
def validate_project_number(request):
    project_number = request.GET.get('project_number', None).strip()
    data = { 'is_taken':False}





        # FOR ALLOWING PERSON WHO IS ASSESSING THE PROJECT, TO PURCHASE THE PRODUCT,
        # LETTING PURCHASE PASS WITHOUT CONSULTATION

    # if Appointment.objects.filter(project_number=project_number).exists() and \
    #         not Appointment.objects.get(project_number=project_number).done:
    #         data = {
    #             'is_taken': True,
    #             'msg': 'We did not have consultation yet! '
    #         }

    # check if it is already used and paid for
    if Order.objects.filter(project_number=project_number).exists() and \
                     Appointment.objects.get(project_number=project_number).paid_for:
        data = {
            'is_taken': True,
            'msg': 'This Project ID is already paid for. \
                       If you need new project, please book free consultation first.'
        }
     # check if consultation took place and is marked as done
    elif Appointment.objects.filter(project_number=project_number).exists() and \
                    not Appointment.objects.get(project_number=project_number).done:
        data = {
                    'no_consultation': True,
                    'msg': 'We did not have consultation yet! We will let you purchase the product '
                           'as this is testing site and we can not have consultation, but in real life '
                           'scenario, we would have to have conversation about your project, to see '
                           'if we can help you with your idea. '
                }
    # check if appointment exists
    elif not Appointment.objects.filter(project_number=project_number).exists():
        data = {
            'is_taken': True,
            'msg': 'We can not find your Project ID in our database. \
                   If you need new project, please book free consultation first.'
        }



    return JsonResponse(data)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]

        # check if we have appointment with this id

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
            'project_number': request.POST.get('project_number'),
            'street1': request.POST.get('street1'),
            'city': request.POST.get('city'),
            'post_code': request.POST.get('post_code'),
            'country': request.POST.get('country'),
            'email': request.POST.get('email'),
            'product_type': product_type,
            'grand_total': total,
        }
        order_form = OrderForm(form_data)
        # new paid consultation doesn't need project id

        # check if we have appointment with this id
        if not Appointment.objects.filter(project_number=request.POST.get('project_number').strip()).exists():
            messages.error(request, 'We can not find your Project ID in our database. \
                                                                          Please double check your information.')
            context['order_form'] = order_form
            return render(request, template, context)

        # check if it is already used and paid for
        if Order.objects.filter(project_number=request.POST.get('project_number').strip()).exists():
            messages.error(request, 'This Project ID is already paid for. \
                                                                          Please double check your information.')

            context['order_form'] = order_form
            return render(request, template, context)

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

                # create new project for the order with project number created
                # when appointment was created so that appointment, order and project are
                # all connected through project number
                ProjectForm({'project_number': request.POST.get('project_number')}).save()

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
