from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from appointments.forms import AppointmentForm
from appointments.models import Appointment
from checkout.models import Order
from freelancers.models import Freelancer
from send_mail.views import send_mail


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
            'site_type': request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'notes': request.POST['notes'],
            'done': 'done' in request.POST,
        }

        appointment_form = AppointmentForm(form_data)
        context = {
            'form': appointment_form
        }
        # user already registered with his email
        if not request.user.is_authenticated and user_email_present(request.POST['email']):
            messages.error(request,
                           'It appears that you already registered.Please login with '
                           ' your credentials to manage your account. Thank you! '
                           )

            return render(request, template, context)

        # username used already, Django won't create new user with the same name
        if not request.user.is_authenticated and user_name_present(request.POST['name']):
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
                appointment_form = appointment_form.save()

                if user_email_present(request.POST['email']):
                    messages.info(request,
                                  'It appears that you already registered. We added this  '
                                  ' consultation to your dashboard. Thank you! '
                                  )
                else:
                    # create new user if not registered yet
                    new_user = User.objects.create_user(request.POST['name'],
                                                        request.POST['email'],
                                                        request.POST['password'])
                    new_user.save()

                messages.success(request,
                                 f'Your account was created successfully. Please login with your '
                                 'credentials.')
                # user can sign in with his credentials

                # sending email to owner of the website, informing him about new appointment
                send_mail(
                    {
                        'to': 'marcelkolarcik@gmail.com',
                        'subject': 'New appointment',
                        'template': 'marcellidesigns_appointment',
                        'template_vars': {'welcome': 'New appointment : ' + request.POST['site_type'],
                                          'body_1': request.POST['email'] + ' - ' + request.POST['phone_num'] + ' - ' +
                                                    request.POST[
                                                        'name'],
                                          'body_2': request.POST['project'],
                                          'question': request.POST['time_slot'],
                                          'sign-in': 'Site',
                                          'welcome_team': 'Marcelli Designs', }
                    })

                # sending email to customer, informing him about new appointment

                send_mail(
                    {
                        'to': request.POST['email'],
                        'subject': 'Your appointment',
                        'template': 'marcellidesigns_customer_appointment',
                        'template_vars': {'welcome': 'Your appointment',
                                          'customer_name': request.POST['name'],
                                          'time': request.POST['time_slot'],
                                          'phone': request.POST['phone_num'],
                                          'project': request.POST['project'],
                                          'site_type': request.POST['site_type'],
                                          'welcome_team': 'Marcelli Designs', }
                    })
                return redirect(reverse('account_login'))

            except:
                messages.error(request, 'There was an error with your form. \
                                                              Please double check your information')
        else:
            messages.error(request, 'There was an error with your form. \
                                                                          Please double check your information')
        context['consultation_form'] = appointment_form

    return render(request, template, context)


# client or freelancer updating appointment / communicating through appointment form
@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # if freelancers is trying access project he is not working on => forbidden
    if Freelancer.objects.filter(email=request.user.email).exists() and \
            Freelancer.objects.get(email=request.user.email).current_project != appointment.project_number:
        return HttpResponseForbidden()

    # if client is not owner of the appointment  => forbidden
    if not Freelancer.objects.filter(email=request.user.email).exists() and appointment.email != request.user.email:
        return HttpResponseForbidden()
    try:
        freelancer = Freelancer.objects.get(current_project=appointment.project_number)
    except:
        freelancer = False

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            return render(request, 'public_user/index.html')

    form = AppointmentForm(instance=appointment)
    context = {
        'paid_for':appointment.paid_for,
        'form': form,
        'appointment_id': appointment_id,
        'email': appointment.email,
        'freelancer': freelancer
    }
    return render(request, 'appointments/edit_appointment.html', context)

# customer deleting appointment
def delete_appointment(request, appointment_id):
    try:
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        messages.success(request, "Your appointment was deleted successfully!")

    except:
        messages.error(request, "Appointment does not exist")

    return redirect('profile')
    #return render(request, 'appointments/profile.html', {})

"""
    user can log in to his account to update or delete appointment
    to see his orders if any, to see progress of the work on his project
"""


@login_required
def profile(request):
    # if user is freelancer we will redirect to freelancer dashboard
    if Freelancer.objects.filter(email=request.user.email).exists():

        return redirect(reverse('freelancer'))

    else:
        template = 'appointments/profile.html'
        request.session["client"] = True

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
        'email': request.user.email,

    }

    return render(request, template, context)
