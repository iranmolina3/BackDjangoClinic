from django.urls import path
from .views import *

urlpatterns = [
    path('create_rol/', create_rol, name = 'create_rol')
]