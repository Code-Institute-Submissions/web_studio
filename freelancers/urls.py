from django.urls import path

from .views import register_form, register_freelancer, freelancer, update_freelancer

urlpatterns = [

    path('register_form/', register_form, name='register_form'),
    path('register_freelancer/', register_freelancer, name='register_freelancer'),
    path('update_freelancer/<freelancer_id>', update_freelancer, name='update_freelancer'),
    path('freelancer/', freelancer, name='freelancer'),

]
