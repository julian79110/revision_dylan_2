# Generated by Django 5.0 on 2023-12-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0012_remove_predio_propietarios_predio_propietarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='propietarios',
            field=models.ManyToManyField(to='predio.propietario'),
        ),
    ]
