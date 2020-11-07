from django import forms
from .models import *

class FormRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre', 'estado'
        ]

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre', 'apellido', 'dpi', 'edad', 'telefono', 'genero',
            'fecha_nacimiento', 'estado',
        ]

class FormPregunta(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'descripcion', 'estado'
        ]

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'carnet', 'contrasena', 'email', 'estado',
            'fk_persona', 'fk_rol'
        ]

class FormCsat(forms.ModelForm):
    class Meta:
        model = Nps
        fields = [
            'respuesta', 'estado', 'fk_pregunta'
        ]

class FormTipoEstado(forms.ModelForm):
    class Meta:
        model = TipoEstado
        fields = [
            'nombre', 'estado'
        ]

class FormCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'numero', 'estado', 'fk_persona'
        ]

class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'motivo_consulta', 'historia', 'estado'
        ]

class FormExamenFisico(forms.ModelForm):
    class Meta:
        model = ExamenFisico
        fields = [
            'presion_arterial', 'frecuencia_cardiaca', 'frecuencia_respitaroria',
            'temperatura', 'frecuencia_cardiaca_fetal', 'impresion_clinica', 'estado'
        ]

class FormAntecedente(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = [
            'ultima_regla', 'fecha_probable_parto', 'gesta', 'aborto', 'hijos_vivos',
            'peso', 'quirurgico', 'medico', 'alergia', 'familiar', 'habito', 'cigarro', 'licor', 'estado'
        ]