
from django.contrib import admin
from django.urls import path
from public.views import index,blog,get_in_touch,website,online_store

urlpatterns = [

    path('',index,name='home'),
    path('get-in-touch', get_in_touch, name='get_in_touch'),
    path('blog', blog, name='blog'),
    path('website', website, name='website'),
    path('online-store', online_store, name='online_store'),

]
