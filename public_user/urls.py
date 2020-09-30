from django.urls import path

from public_user.views import index, portfolio, howitworks

urlpatterns = [

    path('', index, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('how-it-works/', howitworks, name='howitworks'),

]
