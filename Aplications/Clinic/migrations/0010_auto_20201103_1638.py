# Generated by Django 2.1 on 2020-11-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0009_auto_20201103_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedente',
            name='aborto',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='fecha_probable_parto',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='gesta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='ultima_regla',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]