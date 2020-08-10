from django.db import models

# Create your models here.

# Create table rol

class Rol(models.Model):
    PK_ROL = models.AutoField(primary_key = True)
    NOMBRE = models.CharField(max_length=25, blank=False, null=False)
    ESTADO = models.BooleanField(default=True, blank=False, null=False)

