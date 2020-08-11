from django.db import models
from django.utils.timezone import now
# Create your models here.

# Create table rol

class Rol(models.Model):
    PK_ROL = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['NOMBRE']

    def __str__(self):
        return "{0},{1}".format(self.NOMBRE, self.ESTADO)

class EstadoCivil(models.Model):
    PK_ESTADO_CIVIL = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'
        ordering = ['NOMBRE']

    def __str__(self):
        return "{0},{1}".format(self.NOMBRE, self.ESTADO)

class Municipio(models.Model):
    PK_MUNICIPIO = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['NOMBRE']

    def __str__(self):
        return "{0},{1}".format(self.NOMBRE, self.ESTADO)

class Direccion(models.Model):
    PK_DIRECCION = models.AutoField(primary_key=True)
    DESCRIPCION = models.TextField(blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_MUNICIPIO = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return "{0},{1},{2}".format(self.FK_MUNICIPIO, self.DESCRIPCION, self.ESTADO)

class Persona(models.Model):
    PK_PERSONA = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=50, blank=False, null=False)
    APELLIDO = models.CharField(max_length=50, blank=False, null=False)
    DPI = models.CharField(max_length=14, default='Menor de edad', blank=False, null=False)
    EDAD = models.IntegerField(blank=False, null=False)
    FECHA = models.DateField(auto_now=False, auto_now_add=True)
    TELEFONO = models.CharField(max_length=9, blank=True, null=True)
    GENERO = models.CharField(max_length=10, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_DIRECCION = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=False, null=False)
    FK_ESTADO_CIVIL = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['FECHA']

    def __str__(self):
        return "{0},{1},{2}".format(self.NOMBRE, self.APELLIDO, self.FECHA, self.ESTADO)

class Pregunta(models.Model):
    PK_PREGUNTA = models.AutoField(primary_key=True)
    DESCRIPCION = models.CharField(max_length=200, blank=False, null=False)
    FECHA_CREACION = models.DateField(auto_now_add=True, auto_now=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        ordering = ['FECHA_CREACION']

    def __str__(self):
        return "{0},{1},{2}".format(self.DESCRIPCION, self.ESTADO, self.FECHA_CREACION)

class Usuario(models.Model):
    PK_USUARIO = models.AutoField(primary_key=True)
    CARNET = models.CharField(max_length=60, blank=False, null=False)
    CONTRASENIA = models.CharField(max_length=25, blank=False, null=False)
    FECHA_CREACION = models.DateField(auto_now=False, auto_now_add=True)
    CORREO = models.EmailField(default='nocorreo@dominio.com', blank=True, null=True)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    FK_ROL = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['FECHA_CREACION']

    def __str__(self):
        return "{0},{1},{2}".format(self.CARNET, self.CORREO, self.FECHA_CREACION)

class HistorialCsat(models.Model):
    PK_HISTORIAL_CSAT = models.AutoField(primary_key=True)
    RESPUESTA = models.IntegerField(blank=False, null=False)
    FECHA_CREACION = models.DateField(auto_now_add=True, auto_now=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_PREGUNTA = models.ForeignKey(Pregunta, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'HistorialCsat'
        verbose_name_plural = 'HistorialCsat'
        ordering = ['FECHA_CREACION']

    def __str__(self):
        return "{0},{1},{2}".format(self.FK_PREGUNTA, self.RESPUESTA, self.FECHA_CREACION)

class TipoCita(models.Model):
    PK_TIPO_CITA =  models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=50, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo Cita'
        verbose_name_plural = 'Tipos Citas'
        ordering = ['NOMBRE']

    def __str__(self):
        return "{0},{1}".format(self.NOMBRE, self.ESTADO)


class Cita(models.Model):
    PK_CITA = models.AutoField(primary_key=True)
    NUMERO = models.IntegerField(blank=False, null=True)
    FECHA_CREACION = models.DateTimeField(auto_now_add=True, auto_now=False)
    FECHA_FINALIZACION = models.DateTimeField(auto_now=True)
    ESTADO  = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['NUMERO']

    def __str__(self):
        return "{0},{1},{2}".format(self.NUMERO, self.ESTADO, self.FECHA_FINALIZACION)