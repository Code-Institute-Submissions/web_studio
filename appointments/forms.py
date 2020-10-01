from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'time_slot', 'site_type', 'project', 'password', 'done', 'phone_num')
