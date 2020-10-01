from django.urls import path

from .views import project, edit_project

urlpatterns = [

    path('project/<project_id>', project, name='project'),
    path('edit_project/<project_id>', edit_project, name='edit_project'),


]
