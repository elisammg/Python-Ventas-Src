# Generated by Django 2.2 on 2020-05-27 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Fabricas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VEHICULO',
            fields=[
                ('id_Vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('Marca', models.CharField(max_length=200)),
                ('Linea', models.CharField(max_length=200)),
                ('Anio', models.CharField(max_length=200)),
                ('Codigo_Universal', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='REPUESTOS',
            fields=[
                ('Codigo_Repuesto', models.AutoField(primary_key=True, serialize=False)),
                ('Modelo_De_Parte', models.IntegerField(default=0)),
                ('Nombre', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(default=0, max_length=200)),
                ('Stock', models.IntegerField(default=0)),
                ('Precio_Fabricante', models.FloatField(default=0.0)),
                ('Precio_Venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('Fabrica', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Fabricas.FABRICA')),
                ('Vehiculo_Compatible', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Repuestos.VEHICULO')),
            ],
        ),
    ]
