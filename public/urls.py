
from django.contrib import admin
from django.urls import path
from public.views import index

urlpatterns = [

    path('',index,name='hello'),

]
