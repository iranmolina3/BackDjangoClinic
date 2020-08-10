from django.db import models

# Create your models here.

# Create table rol

class Rol(models.Model):
    PK_ROL = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.NOMBRE

class EstadoCivil(models.Model):
    PK_ESTADO_CIVIL = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'

    def __str__(self):
        return self.NOMBRE

class Municipio(models.Model):
    PK_MUNICIPIO = models.AutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.NOMBRE
