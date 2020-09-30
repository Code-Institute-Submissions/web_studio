from django.urls import path

from products.views import blog, website, online_store

urlpatterns = [

    path('blog/', blog, name='blog'),
    path('website/', website, name='website'),
    path('online-store/', online_store, name='online_store'),

]
