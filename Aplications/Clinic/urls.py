from django.urls import path
from .views import *

urlpatterns = [
    path('bienvenido/', Bienvenido, name='urlBienvenido'),
    path('sesion/', Sesion, name='urlSesion'),
]