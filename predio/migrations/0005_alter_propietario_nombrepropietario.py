# Generated by Django 5.0 on 2023-12-27 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0004_remove_predio_propietario_predio_propietarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='nombrePropietario',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='predio.predio'),
        ),
    ]
