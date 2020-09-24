from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('name','email', 'time_slot', 'site_type','project','password','done' )
        password = forms.CharField(widget=forms.PasswordInput)


