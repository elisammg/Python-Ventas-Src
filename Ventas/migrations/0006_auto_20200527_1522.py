# Generated by Django 2.2 on 2020-05-27 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0005_auto_20200527_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Cliente',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cientes.Clientes'),
        ),
    ]
