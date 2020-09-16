
from django.contrib import admin
from django.urls import path
from checkout.views import checkout

urlpatterns = [

    path('<str:type>/',checkout,name='checkout'),


]
