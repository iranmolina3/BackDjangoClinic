from django.contrib import admin
from .models import Rol, EstadoCivil, Municipio

# Register your models here.

admin.site.register(Rol)
admin.site.register(EstadoCivil)
admin.site.register(Municipio)