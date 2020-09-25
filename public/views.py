from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import AppointmentForm
from .models import Appointment


def index(request):
    return render(request, 'public/index.html')


def blog(request):
    return render(request, 'public/blog.html')


def website(request):
    return render(request, 'public/website.html')


def online_store(request):
    return render(request, 'public/online_store.html')


def testimonials(request):
    return render(request, 'public/testimonials.html')


def portfolio(request):
    return render(request, 'public/portfolio.html')


@login_required
def profile(request):
    """
    user can log in to his account to update or delete appointment
    """

    template = 'public/profile.html'

    consultation_detail = Appointment.objects.get(email=request.user.email)

    context = {
        'user': request.user.username,
        'consultations': consultation_detail

    }

    return render(request, template, context)


"""
POTENTIAL CUSTOMER CAN BOOK FREE CONSULTATION
"""


def consultations(request):
    template = 'public/consultation.html'
    context = {}

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

        consultation_form = AppointmentForm(form_data)
        context = {
            'form': consultation_form
        }
        if user_name_present(request.POST['name']):
            messages.error(request, 'Please use different user name !')

            return render(request, template, context)

        if user_email_present(request.POST['email']):
            messages.error(request,
                           'We have user with this email registered already! You can login to see your appointment '
                           ' or use different email to create new appointment.')

            return render(request, template, context)

        if consultation_form.is_valid():
            try:
                """
                IF FORM IS VALID, WE WILL SAVE IT TO DB AND WILL CREATE
                NEW USER WITH CREDENTIALS FROM THE FORM
                SO THAT HE CAN LOG IN INTO HIS ACCOUNT AND 
                CHANGE HIS CONSULTATION
                """
                consultation_form.save()
                new_user = User.objects.create_user(request.POST['name'],
                                                    request.POST['email'],
                                                    request.POST['password'])
                new_user.save()

                messages.success(request, 'Your account was created successfully. Please login with your '
                                          'credentials.')
                """
                user can sign in with his credentials
                """
                return redirect(reverse('account_login'))

            except :
                messages.error(request, 'There was an error with your form. \
                                                              Please double check your information')
        context['consultation_form'] = consultation_form

    return render(request, template, context)


def edit_consultation(request, item_id):
    item = get_object_or_404(Appointment, id=item_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            return render(request, 'public/index.html')

    form = AppointmentForm(instance=item)
    context = {
        'form': form,
        'item_id': item_id,
        'email': item.email
    }
    return render(request, 'public/edit_consultation.html', context)


"""
WHEN USER IS DELETING APPOINTMENT, WE WILL DELETE HIS ACCOUNT AS WELL
"""


def delete_consultation(request, item_id):
    item = get_object_or_404(Appointment, id=item_id)
    item.delete()
    try:
        u = User.objects.get(email=request.user.email)
        u.delete()
        messages.success(request, "Your account and consultation were deleted succesfully")

    except User.DoesNotExist:
        messages.error(request, "User does not exist")

    return redirect('home')
