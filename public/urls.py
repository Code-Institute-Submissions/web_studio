
from django.contrib import admin
from django.urls import path
from public.views import index,blog,get_in_touch,website,online_store,testimonials,consultation,booking_success\
    ,edit_consultation,profile,portfolio

urlpatterns = [

    path('',index,name='home'),
    path('get-in-touch', get_in_touch, name='get_in_touch'),
    path('blog', blog, name='blog'),
    path('website', website, name='website'),
    path('online-store', online_store, name='online_store'),
    path('testimonials', testimonials, name='testimonials'),
    path('portfolio', portfolio, name='portfolio'),
    path('consultation', consultation, name='consultation'),
    path('edit_consultation', edit_consultation, name='edit_consultation'),
    path('booking_success', booking_success, name='booking_success'),
    path('profile', profile, name='profile'),


]
