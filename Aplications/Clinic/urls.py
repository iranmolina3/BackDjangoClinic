from django.urls import path
from .views import *

urlpatterns = [
    # model persona
    path('create_persona/', create_persona, name='create_persona'),
    path('read_persona/', read_persona, name='read_persona'),
    path('update_persona/<int:pk_persona>', update_persona, name='update_persona'),
    path('delete_persona/<int:pk_persona>', delete_persona, name='delete_persona'),
    # model servicio
    path('create_servicio/', create_servicio, name='create_servicio'),
    path('read_servicio/', read_servicio, name='read_servicio'),
    path('update_servicio/<int:pk_servicio>', update_servicio, name='update_servicio'),
    path('delete_servicio/<int:pk_servicio>', delete_servicio, name='delete_servicio'),
    path('updatePersona/<int:pk_historial_clinico>', updatePersona, name='updatePersona'),
    # model cita
    path('create_cita/', create_cita, name='create_cita'),
    path('read_cita/', read_cita, name='read_cita'),
    path('update_cita/<int:pk_cita>', update_cita, name='update_cita'),
    path('delete_cita/<int:pk_cita>', delete_cita, name='delete_cita'),
    # model hisotrio clinico
    path('create_historial_clinico/<int:pk_persona>/<int:pk_cita>', create_historial_clinico,
         name='create_historial_clinico'),
    path('read_historial_clinico/', read_historial_clinico, name='read_historial_clinico'),
    path('delete_historial_clinico/<int:pk_historial_clinico>/<int:pk_cita>', delete_historial_clinico,
         name='delete_historial_clinico'),
    # model consulta
    path('create_consulta/<int:pk_historial_clinico>', create_consulta, name='create_consulta'),
    path('read_consulta/', read_consulta, name='read_consulta'),
    path('update_consulta/<int:pk_consulta>', update_consulta, name='update_consulta'),
    path('delete_consulta/<int:pk_consulta>', delete_consulta, name='delete_consulta'),
    # model antecedente
    path('create_antecedente/<int:pk_historial_clinico>/<int:tipo_antecedente>', create_antecedente,
         name='create_antecedente'),
    path('read_antecedente/', read_antecedente, name='read_antecedente'),
    path('update_antecedente/<int:pk_antecedente>/<int:tipo_antecedente>', update_antecedente,
         name='update_antecedente'),
    path('delete_antecedente/<int:pk_antecedente>', delete_antecedente, name='delete_antecedente'),
    # model examen fisico
    path('create_examen_fisico/<int:pk_historial_clinico>/<int:tipo_examen_fisico>', create_examen_fisico,
         name='create_examen_fisico'),
    path('read_examen_fisico/', read_examen_fisico, name='read_examen_fisico'),
    path('update_examen_fisico/<int:pk_examen_fisico>/<int:tipo_examen_fisico>', update_examen_fisico,
         name='update_examen_fisico'),
    path('delete_examen_fisico/<int:pk_examen_fisico>', delete_examen_fisico, name='delete_examen_fisico'),
    # model recetario
    path('create_receta/<int:pk_historial_clinico>', create_receta, name='create_receta'),
    path('delete_receta/<int:pk_receta>/<int:pk_historial_clinico>', delete_receta, name='delete_receta'),
    # model medicamento
    path('create_medicamento/', create_medicamento, name='create_medicamento'),
    path('read_medicamento/', read_medicamento, name='read_medicamento'),
    path('update_medicamento/<int:pk_medicamento>', update_medicamento, name='update_medicamento'),
    path('delete_medicamento/<int:pk_medicamento>', delete_medicamento, name='delete_medicamento'),
    # model pregunta
    path('create_pregunta/', create_pregunta, name='create_pregunta'),
    path('read_pregunta/', read_pregunta, name='read_pregunta'),
    path('update_pregunta/<int:pk_pregunta>', update_pregunta, name='update_pregunta'),
    path('delete_pregunta/<int:pk_pregunta>', delete_pregunta, name='delete_pregunta'),
    # dashboard
    path('dashboardFiltermonth/<int:month>', dashboardFiltermonth, name='dashboardFiltermonth'),
    # model control clinic
    path('control_clinica/', control_clinica, name='control_clinica'),
    path('estado_servicio_control_clinica/<int:estado_servicio>', estado_servicio_control_clinica,
         name='estado_servicio_control_clinica'),
    # tutorial
    path('show_tutorial/', show_tutorial, name='show_tutorial'),
]
