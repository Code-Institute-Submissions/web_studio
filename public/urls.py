
from django.contrib import admin
from django.urls import path
from public.views import index,blog,get_in_touch,website,online_store,testimonials,edit_consultation,booking_success\
    ,consultations,profile,portfolio,edit_item,delete_item

urlpatterns = [

    path('',index,name='home'),
    path('get-in-touch', get_in_touch, name='get_in_touch'),
    path('blog', blog, name='blog'),
    path('website', website, name='website'),
    path('online-store', online_store, name='online_store'),
    path('testimonials', testimonials, name='testimonials'),
    path('portfolio', portfolio, name='portfolio'),
    path('consultations', consultations, name='consultations'),
    path('edit/consultation/<item_id>', edit_item, name='edit_item'),

    path('delete/consultation/<item_id>', delete_item, name='delete_item'),
    path('edit_consultation', edit_consultation, name='edit_consultation'),
    path('booking_success', booking_success, name='booking_success'),
    path('profile', profile, name='profile'),



]
