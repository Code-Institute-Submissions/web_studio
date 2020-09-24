import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from flask import jsonify

from .models import Appointment
from .forms import AppointmentForm



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
    try:
        consultation_detail = Appointment.objects.get(email=request.user.email)
    except:
        return render(request, 'public/no_consultation.html')



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



def consultations(request):

    template = 'public/consultation.html'
    context ={}

    if request.method == 'POST':

        def user_name_present(name):
            if User.objects.filter(username=name).exists():
                return True

            return False



        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_num': request.POST['phone_num'],
            'password': 'user_password',
            'site_type':  request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'done':  'done' in request.POST,
        }

        consultation_form = AppointmentForm(form_data)
        context = {
            'form':consultation_form
        }
        if user_name_present(request.POST['name']):
            messages.error(request, 'Please use different user name !')

            #return redirect(reverse('consultations'))
            return render(request, template, context)


        if consultation_form.is_valid():
            # try:

                consultation_form.save()




                new_user = User.objects.create_user(request.POST['name'] ,
                                                    request.POST['email'],
                                                    request.POST['password'])
                new_user.save()

                messages.success(request, 'Your account was created successfully \ Please login with your '
                                          'credentials.')

                return redirect(reverse('profile'))



            # except:
            #     messages.error(request, 'There was an error with your form. \
            #                                                   Please double check your information.')
        context['consultation_form'] = consultation_form

    return render(request, template,context)
def edit_item(request, item_id):
    item = get_object_or_404(Appointment, id=item_id)
    if item.email != request.user.email:
        return 'not yours'
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
        'item_id':item_id,
        'email':item.email
    }
    return render(request, 'public/edit_consultation.html', context)
def delete_item(request, item_id):
    item = get_object_or_404(Appointment, id=item_id)
    item.delete()
    try:
        u = User.objects.get(email=request.user.email)
        u.delete()
        messages.success(request, "Your account and consultation were deleted succesfully")

    except User.DoesNotExist:
        messages.error(request, "User does not exist")

    return redirect('home')



def edit_consultation(request):

    template = 'public/profile.html'
    context = {

    }

    if request.method == 'POST':

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_num': request.POST['phone_num'],
            'password': 'user_password',
            'site_type':  request.POST['site_type'],
            'time_slot': request.POST['time_slot'],
            'project': request.POST['project'],
            'done':  'done' in request.POST,



        }

        consultation_form = AppointmentForm(form_data)

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
