from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.urls import reverse

from appointments.models import Appointment
from freelancers.models import Freelancer
from projects.forms import ProjectForm
from projects.models import Project


@login_required
def project(request, project_id):
    # if user is not owner of the project return forbidden
    if Appointment.objects.get(email=request.user.email, project_number=project_id).project_number != project_id:
        return HttpResponseForbidden()

    current_project = Project.objects.get(project_number=project_id)
    context = {
        'project': current_project
    }
    return render(request, 'projects/preview.html', context)


@login_required
def edit_project(request, project_id):
    # if freelancer is not working on the project return forbidden
    if Freelancer.objects.filter(email=request.user.email).exists() and \
            Freelancer.objects.get(email=request.user.email).current_project != project_id:
        return HttpResponseForbidden()

    # if user is not owner of the project return forbidden
    elif not Freelancer.objects.filter(email=request.user.email).exists() and \
            Appointment.objects.get(email=request.user.email).project_number != project_id:
        return HttpResponseForbidden()

    project_i = get_object_or_404(Project, project_number=project_id)
    if request.method == 'POST':

        form = ProjectForm(request.POST, instance=project_i)

        if form.is_valid():
            form = form.save()
            messages.success(request,
                             f'Details updated successfully!{form} '

                             )
            return redirect(reverse('freelancer'))


        else:
            messages.error(request,
                           'There is something wrong with your form '
                           ' Please check your input! '
                           )

            return render(request, 'freelancers/dashboard.html', {'form': form})
