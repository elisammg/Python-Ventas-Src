# Generated by Django 2.2 on 2020-05-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50),
        ),
    ]