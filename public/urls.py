
from django.contrib import admin
from django.urls import path
from public.views import index,blog,website,online_store,testimonials\
    ,consultations,profile,portfolio,edit_consultation,delete_consultation,howitworks

urlpatterns = [

    path('',index,name='home'),
    path('blog', blog, name='blog'),
    path('website', website, name='website'),
    path('online-store', online_store, name='online_store'),
    path('testimonials', testimonials, name='testimonials'),
    path('portfolio', portfolio, name='portfolio'),
    path('how-it-works', howitworks, name='howitworks'),
    path('consultations', consultations, name='consultations'),
    path('edit/consultation/<item_id>', edit_consultation, name='edit_consultation'),
    path('delete/consultation/<item_id>', delete_consultation, name='delete_consultation'),

    path('profile', profile, name='profile'),



]
