# Generated by Django 5.0 on 2023-12-27 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_alter_propietario_nombrepropietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='propietarios',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='predios', to='predio.propietario'),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='nombrePropietario',
            field=models.CharField(default='sin propietario', max_length=30),
        ),
    ]
