"""web_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from appointments import views
from checkout.views import validate_project_number

urlpatterns = [
                  # user needs to make consultation to be able to have an account
                  # so redirecting to appointment page if he types in accounts/signup/ in the browser
                  path('accounts/signup/', views.appointments, name='appointments'),

                  path('validate_project_number/', validate_project_number,
                       name='validate_project_number'),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('checkout/', include('checkout.urls')),
                  path('', include('public_user.urls')),
                  path('', include('products.urls')),
                  path('', include('appointments.urls')),
                  path('', include('freelancers.urls')),
                  path('', include('projects.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
