from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create table rol

class Rol(models.Model):
    pk_rol = models.AutoField('Id del rol', primary_key=True)
    nombre = models.CharField('Nombre del rol', max_length=25, blank=False, null=False)
    estado = models.BooleanField('Estado activo/incativo', default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return "{0},{1}".format(self.nombre, self.estado)


class Persona(models.Model):
    pk_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    dpi = models.CharField(max_length=14, default="--MENOR DE EDAD--", blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    genero = models.CharField(max_length=10, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    estado_civil = models.CharField(default="Soltero(a)", max_length=10, blank=True, null=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_final = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['pk_persona']

    def __str__(self):
        return "{0},{1},{2}".format(self.pk_persona, self.nombre, self.apellido)


class Usuario(models.Model):
    pk_usuario = models.AutoField(primary_key=True)
    carnet = models.CharField(max_length=60, blank=False, null=False)
    contrasena = models.CharField(max_length=25, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    email = models.EmailField(default='nocorreo@dominio.com', blank=True, null=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    fk_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['fecha_creacion']

    def __str__(self):
        return "{0}".format(self.carnet)


class TipoEstado(models.Model):
    pk_tipo_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    estado = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo estado'
        verbose_name_plural = 'Tipos estados'
        ordering = ['nombre']

    def __str__(self):
        return "{0},{1}".format(self.nombre, self.estado)


class Cita(models.Model):
    pk_cita = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=False, null=True)
    fecha = models.DateField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_finalizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    tipo_estado = models.BooleanField(blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_final = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['fecha']

    def __str__(self):
        return "{0},{1},{2}".format(self.pk_cita, self.estado, self.fecha_finalizacion)


# -- if estado is True is active
# -- if estado is False is deactive

# -- if tipo_estado is True cita is complete
# -- if tipo_estado is False cita is cancel


class Pregunta(models.Model):
    pk_pregunta = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    estado = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        ordering = ['fecha_creacion']

    def __str__(self):
        return "{0},{1}".format(self.descripcion, self.estado)


class Nps(models.Model):
    pk_nps = models.AutoField(primary_key=True)
    respuesta = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    estado = models.BooleanField(default=True, blank=False, null=False)
    fk_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Nps'
        verbose_name_plural = 'Nps'
        ordering = ['respuesta']

    def __str__(self):
        return "{0},{1}".format(self.respuesta, self.fk_pregunta)


class Consulta(models.Model):
    pk_consulta = models.AutoField(primary_key=True)
    motivo_consulta = models.TextField(max_length=200, blank=False, null=False)
    historia = models.TextField(blank=False, null=False)
    estado = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['motivo_consulta']

    def __str__(self):
        return "{0},{1}".format(self.motivo_consulta, self.estado)


class ExamenFisico(models.Model):
    pk_examen_fisico = models.AutoField(primary_key=True)
    presion_arterial = models.IntegerField(blank=True, null=True)
    frecuencia_cardiaca = models.IntegerField(blank=True, null=True)
    frecuencia_respitaroria = models.IntegerField(blank=True, null=True)
    temperatura = models.IntegerField(blank=True, null=True)
    frecuencia_cardiaca_fetal = models.IntegerField(blank=True, null=True)
    impresion_clinica = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    tipo_examen_fisico = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Examene Fisico'
        verbose_name_plural = 'Examenes Fisicos'

    def __str__(self):
        return "{0},{1}".format(self.impresion_clinica, self.estado)


class Antecedente(models.Model):
    pk_antecedente = models.AutoField(primary_key=True)
    ultima_regla = models.DateTimeField(blank=True, null=True)
    fecha_probable_parto = models.DateTimeField(blank=True, null=True)
    gesta = models.DateTimeField(blank=True, null=True)
    aborto = models.DateTimeField(blank=True, null=True)
    hijos_vivos = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    quirurgico = models.TextField(blank=True, null=True)
    medico = models.TextField(blank=True, null=True)
    alergia = models.TextField(blank=True, null=True)
    familiar = models.TextField(blank=True, null=True)
    habito = models.TextField(blank=True, null=True)
    cigarro = models.TextField(blank=True, null=True)
    licor = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    tipo_antecedente = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'

    def __str__(self):
        return "{0},{1}".format(self.pk_antecedente, self.estado)


# tipo_antecedente value 0 is not woman pregnant
# tipo_antecedente value 1 is woman pregnant


class Medicamento(models.Model):
    pk_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del medicamento', max_length=400, blank=True, null=True)
    estado = models.BooleanField('Activa/Desactivada', default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return "{0}".format(self.nombre)


# -- this is a property from model =   unique=True

class HistorialClinico(models.Model):
    pk_historial_clinico = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de paciente', max_length=400, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    estado = models.BooleanField(default=True, blank=False, null=False)
    fk_consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, blank=True, null=True)
    fk_examen_fisico = models.OneToOneField(ExamenFisico, on_delete=models.CASCADE, blank=True, null=True)
    fk_antecedente = models.OneToOneField(Antecedente, on_delete=models.CASCADE, blank=True, null=True)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    fk_nps = models.ForeignKey(Nps, on_delete=models.CASCADE, blank=True, null=True)
    fk_cita = models.OneToOneField(Cita, on_delete=models.CASCADE, blank=True, null=True)
    estado_receta = models.BooleanField(default=False, blank=False, null=False)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_final = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Historial clinico'
        verbose_name_plural = 'Historiales clinicos'

    def __str__(self):
        return "{0},{1},{2}".format(self.pk_historial_clinico, self.fecha_creacion, self.estado)

# DateTimeField.auto_now_add is when create object and save only one time
# DateTimeField.auto_now is when update object and save always

class Receta(models.Model):
    pk_receta = models.AutoField(primary_key=True)
    recomendacion = models.TextField(blank=True, null=True)
    fk_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, blank=True, null=True)
    fk_historialclinico = models.ForeignKey(HistorialClinico, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField('Activa/Desactivada', default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['pk_receta']

    def __str__(self):
        return "{0}".format(self.recomendacion)


class ControlClinica(models.Model):
    pk_control_clinica = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la clinica', max_length=200, blank=False, null=False)
    servicio = models.BooleanField('control atendiendo/no atendiendo', blank=False, null=False)
    estado = models.BooleanField('Activa/Desactivada', blank=False, null=False)

    class Meta:
        verbose_name = 'Control clinica'
        verbose_name_plural = 'Controles clinicas'

    def __str__(self):
        return "{0}".format(self.nombre)
