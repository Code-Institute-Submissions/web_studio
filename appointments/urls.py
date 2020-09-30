from django.urls import path

from appointments.views import appointments, edit_appointment, delete_appointment, profile

urlpatterns = [

    path('appointments/', appointments, name='appointments'),
    path('edit/appointment/<item_id>', edit_appointment, name='edit_appointment'),
    path('delete/appointment/<item_id>', delete_appointment, name='delete_appointment'),
    path('profile/', profile, name='profile'),

]
