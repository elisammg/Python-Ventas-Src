# Generated by Django 2.2 on 2020-05-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricas', '0005_prueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion_fabrica',
            name='Fabricante',
            field=models.CharField(max_length=200, null=True),
        ),
    ]