# Generated by Django 2.2 on 2020-05-27 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='Vendedor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Ventas.Usuario'),
            preserve_default=False,
        ),
    ]
