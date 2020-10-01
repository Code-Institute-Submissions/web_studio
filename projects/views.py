from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from projects.forms import ProjectForm
from projects.models import Project

@login_required
def project(request, project_id):
    current_project = Project.objects.get(project_number=project_id)
    context = {
        'project': current_project
    }
    return render(request, 'projects/preview.html', context)

@login_required
def edit_project(request, project_id):
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

