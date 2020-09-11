from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# IranDev this is the model admin ROL

class ResourceRol(resources.ModelResource):
    class Meta:
        model = Rol

class AdminRol(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NOMBRE']
    list_display = ['NOMBRE', 'ESTADO']
    resource_class = ResourceRol

admin.site.register(Rol, AdminRol)

# IranDev this is the model admin ESTADO_CIVIl

class ResourceEstadoCivil(resources.ModelResource):
    class Meta:
        model = EstadoCivil

class AdminEstadoCivil(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NOMBRE']
    list_display = ['NOMBRE', 'ESTADO']
    resource_class = ResourceEstadoCivil

admin.site.register(EstadoCivil, AdminEstadoCivil)

# IranDev this is the model admin MUNICIPIO

class ResourceMunicipio(resources.ModelResource):
    class Meta:
        model = Municipio

class AdminMunicipio(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NOMBRE']
    list_display = ['NOMBRE', 'ESTADO']
    resource_class = ResourceMunicipio

admin.site.register(Municipio, AdminMunicipio)

# IranDev this is the model admin PERSONA

class ResourcePersona(resources.ModelResource):
    class Meta:
        model = Persona

class AdminPersona(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NOMBRE']
    list_display = ['NOMBRE', 'APELLIDO', 'ESTADO']
    resource_class = ResourcePersona

admin.site.register(Persona, AdminPersona)

# IranDev this is the model admin PREGUNTA

class ResourcePregunta(resources.ModelResource):
    class Meta:
        model = Pregunta

class AdminPregunta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['DESCRIPCION']
    list_display = ['DESCRIPCION', 'ESTADO']
    resource_class = ResourcePregunta

admin.site.register(Pregunta, AdminPregunta)

# IranDev this is the model admin USUARIO

class ResourceUsuario(resources.ModelResource):
    class Meta:
        model = Usuario

class AdminPregunta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['CARNET']
    list_display = ['CARNET', 'FK_PERSONA', 'ESTADO']
    resource_class = ResourceUsuario

admin.site.register(Usuario, AdminPregunta)

# IranDev this is the model admin HISTORIAL_CSAT

class ResourceHistorialCsat(resources.ModelResource):
    class Meta:
        model = HistorialCsat

class AdminHistorialCsat(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['RESPUESTA']
    list_display = ['FK_PREGUNTA', 'RESPUESTA', 'ESTADO']
    resource_class = ResourceHistorialCsat

admin.site.register(HistorialCsat, AdminHistorialCsat)

# IranDev this is the model admin TIPO_CITA

class ResourceTipoEstado(resources.ModelResource):
    class Meta:
        model = TipoEstado

class AdminTipoEstado(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NOMBRE']
    list_display = ['NOMBRE', 'ESTADO']
    resource_class = ResourceTipoEstado

admin.site.register(TipoEstado, AdminTipoEstado)

# IranDev this is the model admin CITA

class ResourceCita(resources.ModelResource):
    class Meta:
        model = Cita

class AdminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NUMERO']
    list_display = [ 'NUMERO', 'FECHA_INGRESO', 'ESTADO', 'FK_PERSONA', 'FK_TIPO_ESTADO']
    resource_class = ResourceCita

admin.site.register(Cita, AdminCita)

# IranDev this is the model admin EXAMEN_FISICO

class ResourceExamenFisico(resources.ModelResource):
    class Meta:
        model = ExamenFisico

class AdminExamenFisico(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['IMPRESION_CLINCIA']
    list_display = ['IMPRESION_CLINCIA', 'ESTADO']
    resource_class = ResourceExamenFisico

admin.site.register(ExamenFisico, AdminExamenFisico)

# IranDev this is the model admin CONSULTA

class ResourceConsulta(resources.ModelResource):
    class Meta:
        model = Consulta

class AdminConsulta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ESTADO']
    list_display = ['MOTIVO_CONSULTA', 'ESTADO']
    resource_class = ResourceConsulta

admin.site.register(Consulta, AdminConsulta)

# IranDev this is the model admin ANTECEDENTE

class ResourceAntecedente(resources.ModelResource):
    class Meta:
        model = Antecedente

class AdminAntecedente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['FAMILIAR', 'ESTADO']
    list_display = ['FAMILIAR', 'ESTADO']
    resource_class = ResourceAntecedente

admin.site.register(Antecedente, AdminAntecedente)

# IranDev this is the model admin ANTECEDENTE

class ResourceHistorialClinico(resources.ModelResource):
    class Meta:
        model = HistorialClinico

class AdminHistorialClinico(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['FECHA_CREACION']
    list_display = ['FECHA_CREACION', 'ESTADO']
    resource_class = ResourceHistorialClinico

admin.site.register(HistorialClinico, AdminHistorialClinico)

