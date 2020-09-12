from django.urls import path
from .views import *

urlpatterns = [
    path('create_persona/', create_persona, name = 'create_persona'),
    path('read_persona/', read_persona, name = 'read_persona'),
    path('update_persona/<int:pk_persona>', update_persona, name = 'update_persona'),
    path('delete_persona/<int:pk_persona>', delete_persona, name = 'delete_persona'),

    path('create_consulta/', create_consulta, name = 'create_consulta'),
    path('read_consulta/', read_consulta, name = 'read_consulta'),
    path('update_consulta/<int:pk_consulta>', update_consulta, name = 'update_consulta'),
    path('delete_consulta/<int:pk_consulta>', delete_consulta, name = 'delete_consulta'),

    path('create_examen_fisico/', create_examen_fisico, name = 'create_examen_fisico'),
    path('read_examen_fisico/', read_examen_fisico, name = 'read_examen_fisico'),
    path('update_examen_fisico/<int:pk_examen_fisico>', update_examen_fisico, name = 'update_examen_fisico'),
    path('delete_examen_fisico/<int:pk_examen_fisico>', delete_examen_fisico, name = 'delete_examen_fisico'),

    path('create_antecedente/', create_antecedente, name = 'create_antecedente'),
    path('read_antecedente/', read_antecedente, name = 'read_antecedente'),
    path('update_antecedente/<int:pk_antecedente>', update_antecedente, name = 'update_antecedente'),
    path('delete_antecedente/<int:pk_antecedente>', delete_antecedente, name = 'delete_antecedente'),

    path('create_buscar/', create_buscar, name ='create_buscar'),
    path('create_cita/<int:pk_persona>', create_cita, name = 'create_cita'),
    path('update_cita/<int:pk_cita>', update_cita, name = 'update_cita'),
    path('delete_cita/<int:pk_cita>', delete_cita, name = 'delete_cita'),

    path('create_historial_clinico/<int:pk_cita>', create_historial_clinico, name = 'create_historial_clinico'),
    path('read_historial_clinico/', read_historial_clinico, name = 'read_historial_clinico'),
    path('update_historial_clinico/<int:pk_historial_clinico>', update_historial_clinico, name = 'update_historial_clinico'),

    path('create_pregunta/', create_pregunta, name = 'create_pregunta'),
    path('read_buscar/', read_buscar, name = 'read_buscar'),
    path('update_pregunta/<int:pk_pregunta>', update_pregunta, name='update_pregunta'),
    path('delete_pregunta/<int:pk_pregunta>', delete_pregunta, name='delete_pregunta'),

    path('read_buscar/', read_buscar, name = 'read_buscar'),
]