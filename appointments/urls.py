from django.urls import path

from appointments.views import appointments, edit_appointment, profile,delete_appointment

urlpatterns = [

    path('appointments/', appointments, name='appointments'),
    path('edit/appointment/<appointment_id>', edit_appointment, name='edit_appointment'),
    path('delete/appointment/<appointment_id>', delete_appointment, name='delete_appointment'),
    path('profile/', profile, name='profile'),

]
