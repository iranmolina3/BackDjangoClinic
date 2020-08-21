from django import forms
from .models import *

class formRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'NOMBRE', 'ESTADO'
        ]

class formEstadoCivil(forms.ModelForm):
    class Meta:
        model = [
            'NOMBRE', 'ESTADO'
        ]

class formMunicipio(forms.ModelForm):
    class Meta:
        model = [
            'NOMBRE', 'ESTADO'
        ]

class formDireccion(forms.ModelForm):
    class Meta:
        model = [
            'DESCRIPCION', 'ESTADO', 'FK_MUNICIPIO'
        ]

class formPersona(forms.ModelForm):
    class Meta:
        model = [
            'NOMBRE', 'APELLIDO', 'DPI', 'EDAD', 'FECHA', 'TELEFONO', 'GENERO',
            'ESTADO', 'FK_DIRECCION', 'FK_ESTADO_CIVIL'
        ]

class formPregunta(forms.ModelForm):
    class Meta:
        model = [
            'DESCRIPCION', 'FECHA_CREACION', 'ESTADO'
        ]

class formUsuario(forms.ModelForm):
    class Meta:
        model = [
            'CARNET', 'CONTRASENIA', 'FECHA_CREACION', 'CORREO', 'ESTADO',
            'FK_PERSONA', 'FK_ROL'
        ]

class formHistorialCsat(forms.ModelForm):
    class Meta:
        model = [
            'RESPUESTA', 'FECHA_CREACION', 'ESTADO', 'FK_PREGUNTA'
        ]

class formTipoCita(forms.ModelForm):
    class Meta:
        model = [
            'NOMBRE', 'ESTADO'
        ]

class formCita(forms.ModelForm):
    class Meta:
        model = [
            'NUMERO', 'FECHA_CREACION', 'FECHA_FINALIZACION', 'ESTADO'
        ]

class formConsulta(forms.ModelForm):
    class Meta:
        model = [
            'MOTIVO_CONSULTA', 'HISTORIA', 'ESTADO'
        ]

class formExamenFisico(forms.ModelForm):
    class Meta:
        model = [
            'PRESION_ARTERIAL', 'FRECUENCIA_CARDIACA', 'FRECUENCIA_RESPIRATORIA',
            'TEMPERATURA', 'FRECUENCIA_CARDIACA_FETAL', 'IMPRESION_CLINCIA', 'ESTADO'
        ]

class formAntecedente(forms.ModelForm):
    class Meta:
        model = [
            'ULTIMA_REGLA', 'FECHA_PROBABLE_PARTO', 'GESTA', 'ABORTO', 'HIJOS_VIVOS',
            'PESO', 'QUIRURGICO', 'MEDICO', 'ALERGIA', 'FAMILIAR', 'HABITO', 'CIGARRO', 'LICOR', 'ESTADO'
        ]

