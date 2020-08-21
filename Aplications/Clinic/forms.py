from django import forms
from .models import *

class FormRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'NOMBRE', 'ESTADO'
        ]

class FormEstadoCivil(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = [
            'NOMBRE', 'ESTADO'
        ]

class FormMunicipio(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = [
            'NOMBRE', 'ESTADO'
        ]

class FormDireccion(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'DESCRIPCION', 'ESTADO', 'FK_MUNICIPIO'
        ]

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'NOMBRE', 'APELLIDO', 'DPI', 'EDAD', 'TELEFONO', 'GENERO',
            'ESTADO', 'FK_DIRECCION', 'FK_ESTADO_CIVIL'
        ]

class FormPregunta(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'DESCRIPCION', 'ESTADO'
        ]

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'CARNET', 'CONTRASENIA', 'CORREO', 'ESTADO',
            'FK_PERSONA', 'FK_ROL'
        ]

class FormHistorialCsat(forms.ModelForm):
    class Meta:
        model = HistorialCsat
        fields = [
            'RESPUESTA', 'ESTADO', 'FK_PREGUNTA'
        ]

class FormTipoCita(forms.ModelForm):
    class Meta:
        model = TipoCita
        fields = [
            'NOMBRE', 'ESTADO'
        ]

class FormCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'NUMERO', 'ESTADO'
        ]

class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'MOTIVO_CONSULTA', 'HISTORIA', 'ESTADO'
        ]

class FormExamenFisico(forms.ModelForm):
    class Meta:
        model = ExamenFisico
        fields = [
            'PRESION_ARTERIAL', 'FRECUENCIA_CARDIACA', 'FRECUENCIA_RESPIRATORIA',
            'TEMPERATURA', 'FRECUENCIA_CARDIACA_FETAL', 'IMPRESION_CLINCIA', 'ESTADO'
        ]

class FormAntecedente(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = [
            'ULTIMA_REGLA', 'FECHA_PROBABLE_PARTO', 'GESTA', 'ABORTO', 'HIJOS_VIVOS',
            'PESO', 'QUIRURGICO', 'MEDICO', 'ALERGIA', 'FAMILIAR', 'HABITO', 'CIGARRO', 'LICOR', 'ESTADO'
        ]

