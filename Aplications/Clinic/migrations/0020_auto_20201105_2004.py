# Generated by Django 2.1 on 2020-11-06 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0019_auto_20201105_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receta',
            options={'ordering': ['pk_receta'], 'verbose_name': 'Receta', 'verbose_name_plural': 'Recetas'},
        ),
        migrations.RemoveField(
            model_name='historialclinico',
            name='fk_receta',
        ),
        migrations.AddField(
            model_name='receta',
            name='fk_historialclinico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Clinic.HistorialClinico'),
        ),
    ]
