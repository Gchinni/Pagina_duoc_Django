# Generated by Django 3.2.5 on 2021-07-14 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_mascota_detalles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='nombre',
        ),
        migrations.AddField(
            model_name='mascota',
            name='nombre_dueno',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='nombre_mascota',
            field=models.CharField(max_length=150, null=True),
        ),
    ]