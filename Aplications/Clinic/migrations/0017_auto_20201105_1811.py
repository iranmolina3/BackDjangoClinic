# Generated by Django 2.1 on 2020-11-06 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0016_auto_20201105_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='nombre',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Nombre del medicamento'),
        ),
    ]
