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
    search_fields = ['nombre']
    list_display = ['nombre', 'estado']
    resource_class = ResourceRol


admin.site.register(Rol, AdminRol)


# IranDev this is the model admin PERSONA

class ResourcePersona(resources.ModelResource):
    class Meta:
        model = Persona


class AdminPersona(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_persona', 'nombre', 'apellido', 'estado', 'hora_inicio', 'hora_final']
    resource_class = ResourcePersona


admin.site.register(Persona, AdminPersona)


# IranDev this is the model admin PREGUNTA

class ResourcePregunta(resources.ModelResource):
    class Meta:
        model = Pregunta


class AdminPregunta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ['descripcion', 'estado']
    resource_class = ResourcePregunta


admin.site.register(Pregunta, AdminPregunta)


# IranDev this is the model admin USUARIO

class ResourceUsuario(resources.ModelResource):
    class Meta:
        model = Usuario


class AdminPregunta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['carnet']
    list_display = ['carnet', 'fk_persona', 'estado']
    resource_class = ResourceUsuario


admin.site.register(Usuario, AdminPregunta)


# IranDev this is the model admin HISTORIAL_CSAT

class ResourceNps(resources.ModelResource):
    class Meta:
        model = Nps


class AdminNps(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['respuesta']
    list_display = ['fk_pregunta', 'respuesta', 'estado']
    resource_class = ResourceNps


admin.site.register(Nps, AdminNps)


# IranDev this is the model admin TIPO_CITA

class ResourceTipoEstado(resources.ModelResource):
    class Meta:
        model = TipoEstado


class AdminTipoEstado(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado']
    resource_class = ResourceTipoEstado


admin.site.register(TipoEstado, AdminTipoEstado)


# IranDev this is the model admin CITA

class ResourceCita(resources.ModelResource):
    class Meta:
        model = Cita


class AdminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['numero']
    list_display = ['pk_cita', 'numero', 'fecha_creacion', 'estado', 'fk_persona', 'hora_inicio', 'hora_final']
    resource_class = ResourceCita


admin.site.register(Cita, AdminCita)


# IranDev this is the model admin EXAMEN_FISICO

class ResourceExamenFisico(resources.ModelResource):
    class Meta:
        model = ExamenFisico


class AdminExamenFisico(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['impresion_clinica']
    list_display = ['impresion_clinica', 'estado']
    resource_class = ResourceExamenFisico


admin.site.register(ExamenFisico, AdminExamenFisico)


# IranDev this is the model admin CONSULTA

class ResourceConsulta(resources.ModelResource):
    class Meta:
        model = Consulta


class AdminConsulta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['estado']
    list_display = ['motivo_consulta', 'estado']
    resource_class = ResourceConsulta


admin.site.register(Consulta, AdminConsulta)


# IranDev this is the model admin ANTECEDENTE

class ResourceAntecedente(resources.ModelResource):
    class Meta:
        model = Antecedente


class AdminAntecedente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['familiar', 'estado']
    list_display = ['familiar', 'estado']
    resource_class = ResourceAntecedente


admin.site.register(Antecedente, AdminAntecedente)


# IranDev this is the model admin ANTECEDENTE

class ResourceHistorialClinico(resources.ModelResource):
    class Meta:
        model = HistorialClinico


class AdminHistorialClinico(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha_creacion']
    list_display = ['pk_historial_clinico', 'fk_persona', 'fecha_creacion', 'estado', 'hora_inicio', 'hora_final']
    resource_class = ResourceHistorialClinico


admin.site.register(HistorialClinico, AdminHistorialClinico)


# Irandev this is a model admin CONTROL_CLINICA

class ResourceControlClinica(resources.ModelResource):
    class Meta:
        model = ControlClinica


class AdminControlClinica(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_display = ['nombre', ]
    resource_class = ResourceControlClinica


admin.site.register(ControlClinica, AdminControlClinica)


# Irandev this is a model admin MEDICAMENTO

class ResourceMedicamento(resources.ModelResource):
    class Meta:
        model = Medicamento


class AdminMedicamento(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', ]
    list_display = ['pk_medicamento', 'nombre', 'estado']
    resource_class = ResourceMedicamento


admin.site.register(Medicamento, AdminMedicamento)

# Irandev this is a model admin

class ResourceReceta(resources.ModelResource):
    class Meta:
        model = Receta


class AdminReceta(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['recomendacion', ]
    list_display = ['pk_receta', 'recomendacion', 'fk_medicamento']
    resource_class = ResourceReceta


admin.site.register(Receta, AdminReceta)
