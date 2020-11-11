"""DevBackDjangoClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import auth_login, logout_then_login
from Aplications.Clinic.views import *
from Aplications.Clinic.urls import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinic/', include(('Aplications.Clinic.urls', 'clinic'))),
    path('', home, name = 'index'),
    path('servicios/', servicios, name='servicios'),
    path('sing/', sing, name ='sing'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout_view/', logout_view, name = 'logout')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
