# Generated by Django 2.1 on 2020-11-04 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0011_auto_20201104_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historialclinico',
            old_name='fk_antecendente',
            new_name='fk_antecedente',
        ),
    ]