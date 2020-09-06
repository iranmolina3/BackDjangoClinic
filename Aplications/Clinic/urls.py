from django.urls import path
from .views import *

urlpatterns = [
    path('create_persona/', create_persona, name = 'create_persona'),
    path('read_persona/', read_persona, name = 'read_persona'),
    path('update_persona/<int:pk_persona>', update_persona, name = 'update_persona'),
    path('delete_persona/<int:pk_persona>', delete_persona, name = 'delete_persona'),
]