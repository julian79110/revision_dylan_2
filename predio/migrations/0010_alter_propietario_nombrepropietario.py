# Generated by Django 5.0 on 2023-12-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0009_alter_predio_propietarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='nombrePropietario',
            field=models.CharField(default='sin propietario', max_length=30, null=True),
        ),
    ]