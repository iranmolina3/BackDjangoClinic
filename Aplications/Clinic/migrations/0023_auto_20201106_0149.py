# Generated by Django 2.1 on 2020-11-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0022_historialclinico_estado_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='descripcion',
            field=models.TextField(),
        ),
    ]