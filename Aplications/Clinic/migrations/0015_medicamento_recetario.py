# Generated by Django 2.1 on 2020-11-05 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0014_auto_20201104_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('pk_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=400, null=True, verbose_name='Nombre del medicamento')),
                ('estado', models.BooleanField(default=True, verbose_name='Activa/Desactivada')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='Recetario',
            fields=[
                ('pk_recetario', models.AutoField(primary_key=True, serialize=False)),
                ('recomendacion', models.TextField(blank=True, null=True)),
                ('fk_medicamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Clinic.Medicamento')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
    ]
