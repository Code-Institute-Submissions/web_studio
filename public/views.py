import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from flask import jsonify

from .models import Order, Consultation
from .forms import ConsultationForm

# Create your views here.
def index(request):

    return render(request, 'public/index.html')


def blog(request):
    return render(request, 'public/blog.html')


def website(request):
    return render(request, 'public/website.html')


def online_store(request):
    return render(request, 'public/online_store.html')


def get_in_touch(request):
    return render(request, 'public/get_in_touch.html')


def testimonials(request):
    return render(request, 'public/testimonials.html')

def portfolio(request):
     return render(request, 'public/portfolio.html')
@login_required
def profile(request):
    template = 'public/profile.html'
    consultation_detail = Consultation.objects.get(name=request.user.username)


    """
    IF WE HAVE ORDER IN THE DATABASE, WE WILL LOG USER IN,
    ELSE IF THERE WAS PROBLEM WITH CHECKOUT, WE WILL
    REDIRECT USER TO no_order.html AND ASK HIM TO 
    TRY AGAIN!
    """
    if consultation_detail:
        context = {
            'user': request.user.username,
            'consultations': consultation_detail

        }
    else:
        template = 'public/index.html'
        context = {
            'user': request.user.username,
            'consultations': consultation_detail

        }



    return render(request, template, context)



def consultation(request):

    template = 'public/consultation.html'
    context = {

    }

    if request.method == 'POST':

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'password': 'user_password',
            'site_type':  request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'done':  'done' in request.POST,



        }

        consultation_form = ConsultationForm(form_data)

        if consultation_form.is_valid():
            try:

                consultation_form.save()
                new_user = User.objects.create_user(request.POST['name'] ,
                                                    request.POST['email'],
                                                    request.POST['password'])
                new_user.save()

                messages.success(request, 'Your account was created successfully \ Please login with your '
                                          'credentials.')

                return redirect(reverse('profile'))



            except:
                messages.error(request, 'There was an error with your form. \
                                                              Please double check your information.')
        context['consultation_form'] = consultation_form

    return render(request, template,context)

def edit_consultation(request):

    template = 'public/profile.html'
    context = {

    }

    if request.method == 'POST':

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'password': 'user_password',
            'site_type':  request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'done':  'done' in request.POST,



        }

        consultation_form = ConsultationForm(form_data)

        if consultation_form.is_valid():
            try:

                consultation_form.save()


                messages.success(request, 'Your consultation was updated successfully')

                return redirect(reverse('profile'))



            except:
                messages.error(request, 'There was an error with your form. \
                                                              Please double check your information.')
        context['consultation_form'] = consultation_form

    return render(request, template,context)




def booking_success(request):
    """
    Handle successful booking
    """


    template = 'public/booking_success.html'


    return render(request, template)
