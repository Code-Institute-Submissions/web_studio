import json
import os

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from appointments.forms import AppointmentForm
from appointments.models import Appointment
from checkout.models import Order


def appointments(request):
    template = 'appointments/appointment.html'
    context = {}
    # customer creating appointment
    if request.method == 'POST':

        def user_name_present(name):
            if User.objects.filter(username=name).exists():
                return True

            return False

        def user_email_present(email):
            if User.objects.filter(email=email).exists():
                return True

            return False

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_num': request.POST['phone_num'],
            'password': 'user_password',
            'site_type': request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'done': 'done' in request.POST,
        }

        appointment_form = AppointmentForm(form_data)
        context = {
            'form': appointment_form
        }
        # user already registered with his email
        if user_email_present(request.POST['email']):
            messages.error(request,
                           'It appears that you already registered.Please login with '
                           ' your credentials to manage your appointment. Thank you! '
                           )

            return render(request, template, context)

        # username used already, Django won't create new user with the same name
        if user_name_present(request.POST['name']):
            messages.error(request, 'User name taken. Please use different user name!')

            return render(request, template, context)

        if appointment_form.is_valid():
            try:
                """
                IF FORM IS VALID, WE WILL SAVE IT TO DB AND WILL CREATE
                NEW USER WITH CREDENTIALS FROM THE FORM
                SO THAT HE CAN LOG IN INTO HIS ACCOUNT AND 
                CHANGE HIS CONSULTATION
                """
                appointment_form.save()
                new_user = User.objects.create_user(request.POST['name'],
                                                    request.POST['email'],
                                                    request.POST['password'])
                new_user.save()

                messages.success(request, 'Your account was created successfully. Please login with your '
                                          'credentials.')
                # user can sign in with his credentials

                # sending email to owner of the website, informing him about new appointment
                site_types = {
                    '1': 'blog', '2': 'website', '3': 'online store', '4': 'something else'
                }
                times = {
                    '1': '8am-12am', '2': '12am-16pm', '3': '16pm-20pm',
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
                            {'welcome': 'New appointment : ' + site_types[request.POST['site_type']],
                             'body_1': request.POST['email'] + ' - ' + request.POST['phone_num'] + ' - ' + request.POST[
                                 'name'],
                             'body_2': request.POST['project'],
                             'question': times[request.POST['time_slot']],
                             'sign-in': 'Site',
                             'welcome_team': 'Marcelli Designs', })
                })

                # sending email to customer, informing him about new appointment

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
                return redirect(reverse('account_login'))

            except:
                messages.error(request, 'There was an error with your form. \
                                                              Please double check your information')
        context['consultation_form'] = appointment_form

    return render(request, template, context)


# customer updating appointment
def edit_appointment(request, item_id):
    item = get_object_or_404(Appointment, id=item_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            return render(request, 'public_user/index.html')

    form = AppointmentForm(instance=item)
    context = {
        'form': form,
        'item_id': item_id,
        'email': item.email
    }
    return render(request, 'appointments/edit_appointment.html', context)


# customer deleting appointment
def delete_appointment(request, item_id):
    try:
        item = get_object_or_404(Appointment, id=item_id)
        item.delete()
        messages.success(request, "Your appointment was deleted successfully!")

    except User.DoesNotExist:
        messages.error(request, "Appointment does not exist")

    return redirect('profile')


"""
    user can log in to his account to update or delete appointment
    or to see his orders if any
"""


@login_required
def profile(request):
    template = 'appointments/profile.html'
    try:
        appointment_detail = Appointment.objects.filter(email=request.user.email).order_by('-date')
    except:
        appointment_detail = False

    try:
        orders = Order.objects.filter(email=request.user.email).order_by('-date')
    except:
        orders = False

    context = {
        'user': request.user.username,
        'consultations': appointment_detail,
        'orders': orders,
        'email': request.user.email
    }

    return render(request, template, context)
