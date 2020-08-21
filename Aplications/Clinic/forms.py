from django import forms
from .models import *

class formRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'PK_ROL', 'NOMBRE', 'ESTADO'
        ]

class formEstadoCivil(forms.ModelForm):
    class Meta:
        model = [
            'PK_ESTADO_CIVIL', 'NOMBRE', 'ESTADO'
        ]

class formMunicipio(forms.ModelForm):
    class Meta:
        model = [
            'PK_MUNICIPIO', 'NOMBRE', 'ESTADO'
        ]

class formDireccion(forms.ModelForm):
    class Meta:
        model = [
            'PK_DIRECCION', 'DESCRIPCION', 'ESTADO', 'FK_MUNICIPIO'
        ]

class formPersona(forms.ModelForm):
    class Meta:
        model = [
            'PK_PERSONA', 'NOMBRE', 'APELLIDO', 'DPI', 'EDAD', 'FECHA', 'TELEFONO', 'GENERO',
            'ESTADO', 'FK_DIRECCION', 'FK_ESTADO_CIVIL'
        ]

class formPregunta(forms.ModelForm):
    class Meta:
        model = [
            'PK_PREGUNTA', 'DESCRIPCION', 'FECHA_CREACION', 'ESTADO'
        ]

class formUsuario(forms.ModelForm):
    class Meta:
        model = [
            'PK_USUARIO', 'CARNET', 'CONTRASENIA', 'FECHA_CREACION', 'CORREO', 'ESTADO',
            'FK_PERSONA', 'FK_ROL'
        ]

class formHistorialCsat(forms.ModelForm):
    class Meta:
        model = [
            'PK_HISTORIAL_CSAT', 'RESPUESTA', 'FECHA_CREACION', 'ESTADO', 'FK_PREGUNTA'
        ]

class formTipoCita(forms.ModelForm):
    class Meta:
        model = [
            'PK_TIPO_CITA', 'NOMBRE', 'ESTADO'
        ]

class formCita(forms.ModelForm):
    class Meta:
        model = [
            'PK_CITA', 'NUMERO', 'FECHA_CREACION', 'FECHA_FINALIZACION', 'ESTADO'
        ]

class formConsulta(forms.ModelForm):
    class Meta:
        model = [
            'PK_CONSULTA', 'MOTIVO_CONSULTA', 'HISTORIA', 'ESTADO'
        ]

class formExamenFisico(forms.ModelForm):
    class Meta:
        model = [
            'PK_EXAMEN_FISICO', 'PRESION_ARTERIAL', 'FRECUENCIA_CARDIACA', 'FRECUENCIA_RESPIRATORIA',
            'TEMPERATURA', 'FRECUENCIA_CARDIACA_FETAL', 'IMPRESION_CLINCIA', 'ESTADO'
        ]

class formAntecedente(forms.ModelForm):
    class Meta:
        model = [
            'PK_ANTECEDENTES', 'ULTIMA_REGLA', 'FECHA_PROBABLE_PARTO', 'GESTA', 'ABORTO', 'HIJOS_VIVOS',
            'PESO', 'QUIRURGICO', 'MEDICO', 'ALERGIA', 'FAMILIAR', 'HABITO', 'CIGARRO', 'LICOR', 'ESTADO'
        ]

