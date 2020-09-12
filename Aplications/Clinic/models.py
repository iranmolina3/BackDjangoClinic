from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create table rol

class Rol(models.Model):
    PK_ROL = models.AutoField('Id del rol', primary_key=True)
    NOMBRE = models.CharField('Nombre del rol', max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField('Estado activo/incativo', default=True, blank=False, null=False)

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


class Persona(models.Model):
    PK_PERSONA = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=50, blank=False, null=False)
    APELLIDO = models.CharField(max_length=50, blank=False, null=False)
    DPI = models.CharField(max_length=14, default="--MENOR DE EDAD--", blank=False, null=False)
    EDAD = models.IntegerField(blank=False, null=False)
    FECHA_NACIMIENTO = models.DateField(blank=False, null=False)
    TELEFONO = models.CharField(max_length=9, blank=True, null=True)
    GENERO = models.CharField(max_length=10, blank=False, null=False)
    DIRECCION = models.CharField(max_length=200, blank=True, null=True)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_MUNICIPIO = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=False, null=False)
    FK_ESTADO_CIVIL = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['FECHA_NACIMIENTO']

    def __str__(self):
        return "{0},{1},{2}".format(self.PK_PERSONA, self.NOMBRE, self.APELLIDO)


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
        return "{0},{1}".format(self.DESCRIPCION, self.ESTADO)


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
        return "{0}".format(self.CARNET)


class TipoEstado(models.Model):
    PK_TIPO_ESTADO = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=50, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo estado'
        verbose_name_plural = 'Tipos estados'
        ordering = ['NOMBRE']

    def __str__(self):
        return "{0},{1}".format(self.NOMBRE, self.ESTADO)


class Cita(models.Model):
    PK_CITA = models.AutoField(primary_key=True)
    NUMERO = models.IntegerField(blank=False, null=True)
    FECHA_INGRESO = models.DateField()
    FECHA_CREACION = models.DateTimeField(auto_now_add=True, auto_now=False)
    FECHA_FINALIZACION = models.DateTimeField(auto_now=True)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    FK_TIPO_ESTADO = models.ForeignKey(TipoEstado, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['NUMERO']

    def __str__(self):
        return "{0},{1},{2}".format(self.NUMERO, self.ESTADO, self.FECHA_FINALIZACION)


class HistorialCsat(models.Model):
    PK_HISTORIAL_CSAT = models.AutoField(primary_key=True)
    RESPUESTA = models.IntegerField(blank=False, null=False)
    FECHA_CREACION = models.DateField(auto_now_add=True, auto_now=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_PREGUNTA = models.ForeignKey(Pregunta, on_delete=models.CASCADE, blank=False, null=False)
    FK_CITA = models.OneToOneField(Cita, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'HistorialCsat'
        verbose_name_plural = 'HistorialCsat'
        ordering = ['FECHA_CREACION']

    def __str__(self):
        return "{0},{1},{2}".format(self.FK_PREGUNTA, self.RESPUESTA, self.FECHA_CREACION)


class Consulta(models.Model):
    PK_CONSULTA = models.AutoField(primary_key=True)
    MOTIVO_CONSULTA = models.CharField(max_length=200, blank=False, null=False)
    HISTORIA = models.TextField(blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['MOTIVO_CONSULTA']

    def __str__(self):
        return "{0},{1}".format(self.MOTIVO_CONSULTA, self.ESTADO)


class ExamenFisico(models.Model):
    PK_EXAMEN_FISICO = models.AutoField(primary_key=True)
    PRESION_ARTERIAL = models.IntegerField(blank=True, null=True)
    FRECUENCIA_CARDIACA = models.IntegerField(blank=True, null=True)
    FRECUENCIA_RESPIRATORIA = models.IntegerField(blank=True, null=True)
    TEMPERATURA = models.IntegerField(blank=False, null=True)
    FRECUENCIA_CARDIACA_FETAL = models.IntegerField(blank=True, null=True)
    IMPRESION_CLINCIA = models.TextField(blank=True, null=True)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Examene Fisico'
        verbose_name_plural = 'Examenes Fisicos'

    def __str__(self):
        return "{0},{1}".format(self.IMPRESION_CLINCIA, self.ESTADO)


class Antecedente(models.Model):
    PK_ANTECEDENTE = models.AutoField(primary_key=True)
    ULTIMA_REGLA = models.DateTimeField()
    FECHA_PROBABLE_PARTO = models.DateTimeField()
    GESTA = models.DateTimeField()
    ABORTO = models.DateTimeField()
    HIJOS_VIVOS = models.IntegerField(blank=True, null=True)
    PESO = models.IntegerField(blank=True, null=True)
    QUIRURGICO = models.TextField(blank=True, null=True)
    MEDICO = models.TextField(blank=True, null=True)
    ALERGIA = models.TextField(blank=True, null=True)
    FAMILIAR = models.TextField(blank=True, null=True)
    HABITO = models.TextField(blank=True, null=True)
    CIGARRO = models.BooleanField(default=False, blank=False, null=False)
    LICOR = models.BooleanField(default=False, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'

    def __str__(self):
        return "{0},{1},{2}".format(self.PK_ANTECEDENTE, self.FAMILIAR, self.ESTADO)


class HistorialClinico(models.Model):
    PK_HISTORIAL_CLINICO = models.AutoField(primary_key=True)
    FECHA_CREACION = models.DateField(auto_now_add=True, auto_now=False)
    FILTRO_NOMBRE_COMPLETO = models.CharField(max_length=200, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)
    FK_CONSULTA = models.ForeignKey(Consulta, on_delete=models.CASCADE, blank=False, null=False)
    FK_EXAMEN_FISICO = models.ForeignKey(ExamenFisico, on_delete=models.CASCADE, blank=False, null=False)
    FK_ANTECEDENTE = models.ForeignKey(Antecedente, on_delete=models.CASCADE, blank=False, null=False)
    FK_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    class Meta:
        verbose_name = 'Historial clinico'
        verbose_name_plural = 'Historiales clinicos'

    def __str__(self):
        return "{0},{1},{2}".format(self.PK_HISTORIAL_CLINICO, self.FECHA_CREACION, self.ESTADO)
