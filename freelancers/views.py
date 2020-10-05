from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from appointments.models import Appointment
from projects.models import Project
from send_mail.views import send_mail
from .forms import FreelancerForm
from .models import Freelancer


def register_form(request):
    template = 'freelancers/register_form.html'
    context = {}
    if request.user.is_authenticated:
        messages.info(request,
                      'Thank you for your interest. It appears that you are  '
                      ' already signed in... If you would like to create new'
                      ' account, please logout and try again. Thank you! '
                      )

        context = {
            'logged_in': True
        }
    return render(request, template, context)


def register_freelancer(request):
    template = 'freelancers/register_form.html'

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
        'skills': request.POST['skills'],
        'portfolio_link': request.POST['portfolio_link'],
        'about': request.POST['about'],

    }

    form = FreelancerForm(form_data)
    context = {
        'form': form
    }
    # user already registered with his email
    if user_email_present(request.POST['email']):
        messages.error(request,
                       'It appears that you already registered.Please login with '
                       ' your credentials to manage your account. Thank you! '
                       )

        return render(request, template, context)

    # username used already, Django won't create new user with the same name
    if user_name_present(request.POST['name']):
        messages.error(request, 'User name taken. Please use different user name!')

        return render(request, template, context)

    if form.is_valid():
        try:
            """
            IF FORM IS VALID, WE WILL SAVE IT TO DB AND WILL CREATE
            NEW USER WITH CREDENTIALS FROM THE FORM
            SO THAT HE CAN LOG IN INTO HIS ACCOUNT
            
            """

            form.save()
            new_user = User.objects.create_user(request.POST['name'],
                                                request.POST['email'],
                                                request.POST['password'])
            new_user.save()

            messages.success(request, 'Your account was created successfully. Please login with your '
                                      'credentials.')
            # send email to new freelancer
            send_mail(
                {
                    'to': request.POST['email'],
                    'subject': 'Welcome to the team!',
                    'template': 'welcome_freelancer',
                    'template_vars': {
                        'name': request.POST['name']
                    }
                })
            # send email to owner of the agency
            send_mail(
                {
                    'to': 'marcelkolarcik@gmail.com',
                    'subject': 'New freelancer to the team!',
                    'template': 'md_new_freelancer',
                    'template_vars': {
                        'name': request.POST['name'],
                        'email': request.POST['email'],
                        'phone_num': request.POST['phone_num'],
                        'skills': request.POST['skills'],
                        'portfolio_link': request.POST['portfolio_link'],
                        'about': request.POST['about'],
                    }
                })

            return redirect(reverse('account_login'))

        except:
            messages.error(request, 'There was an error with your form. \
                                                              Please double check your information')

            context['form'] = form

            return render(request, template, context)
    else:
        messages.error(request, 'There was an error with your form. \
                                                                     Please double check your information')
        context['form'] = form
        return render(request, template, context)


@login_required
def freelancer(request):
    # if logged in client tries to access freelancer page, we will redirect back to client's profile
    if request.session.get('client'):
        return redirect('profile')
    freelancer = Freelancer.objects.get(email=request.user.email)
    form = FreelancerForm(instance=freelancer)
    request.session["freelancer"] = True

    try:
        appointment = Appointment.objects.get(project_number=freelancer.current_project)

    except:
        appointment = False

    try:
        project = Project.objects.get(project_number=freelancer.current_project)
    except:
        project = False

    context = {
        'freelancer': freelancer,
        'form': form,
        'appointment': appointment,
        'project': project
    }
    return render(request, 'freelancers/dashboard.html', context)


@login_required
def update_freelancer(request, freelancer_id):
    freelancer_i = get_object_or_404(Freelancer, id=freelancer_id)
    # if freelancer is not updating his own profile
    if freelancer_i.email != request.user.email:
        return HttpResponseForbidden()

    if request.method == 'POST':

        form = FreelancerForm(request.POST, instance=freelancer_i)

        if form.is_valid():
            form.save()
            messages.success(request,
                             'Details updated successfully! '

                             )
            return redirect(reverse('freelancer'))


        else:
            messages.error(request,
                           'There is something wrong with your form '
                           ' Please check your input! '
                           )

            return render(request, 'freelancers/dashboard.html', {'form': form})
