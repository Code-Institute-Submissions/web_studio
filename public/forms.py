from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('name','email', 'time_slot', 'site_type','project','password','done' )
        password = forms.CharField(widget=forms.PasswordInput)

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'name': 'Full name',
    #         'email': 'Email Address',
    #         'project':'Project',
    #         'password': 'Password',
    #         'time_slot': 'time_slot',
    #         'site_type': 'site_type',
    #         'date': 'date',
    #         'done': 'done',
    #
    #
    #
    #     }
    #
    #     self.fields['name'].widget.attrs['autofocus'] = True
    #     for field in self.fields:
    #         if self.fields[field].required:
    #             placeholder = f'{placeholders[field]} *'
    #         else:
    #             placeholder = placeholders[field]
    #         self.fields[field].widget.attrs['placeholder'] = placeholder
    #
    #         #self.fields[field].widget.attrs['class'] = 'stripe-style-input'
    #         self.fields[field].label = False
