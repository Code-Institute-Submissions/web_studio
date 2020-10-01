from django import forms

from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_number','development_link','started','wireframes','update_after_wireframes',
                  'started_on_site','development_link_sent','client_approved','domain_hosting','done')

