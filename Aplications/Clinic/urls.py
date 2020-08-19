from django.urls import path
from .views import Bienvenido

urlpatterns = [
    path('bienvenido/', Bienvenido, name='urlBienvenido')
]