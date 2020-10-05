from django.urls import path

from checkout.views import checkout, checkout_success, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('wh/', webhook, name='webhook'),

    path('checkout_success/<order_number>',
         checkout_success, name='checkout_success'),

    path('cache_checkout_data/', cache_checkout_data,
         name='cache_checkout_data'),

    path('<str:product_type>/', checkout, name='checkout'),

]
