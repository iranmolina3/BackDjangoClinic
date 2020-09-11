# Generated by Django 2.0 on 2020-09-11 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoCita',
            new_name='TipoEstado',
        ),
        migrations.AlterModelOptions(
            name='tipoestado',
            options={'ordering': ['NOMBRE'], 'verbose_name': 'Tipo estado', 'verbose_name_plural': 'Tipos estados'},
        ),
        migrations.RenameField(
            model_name='tipoestado',
            old_name='PK_TIPO_CITA',
            new_name='PK_TIPO_ESTADO',
        ),
    ]