from django.urls import path
from .views import *

urlpatterns = [
    path('sesion/', login, name='urlSesion'),
]