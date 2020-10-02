from django import forms

from .models import Freelancer


class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('name', 'email', 'about', 'skills', 'portfolio_link','password','phone_num')
