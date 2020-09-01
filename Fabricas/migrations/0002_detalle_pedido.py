# Generated by Django 2.2 on 2020-05-27 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Pedido',
            fields=[
                ('DetalleID', models.AutoField(primary_key=True, serialize=False)),
                ('Productos', models.CharField(max_length=50)),
                ('Cantidad', models.IntegerField(default=0)),
                ('Sub_Total', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('Fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabricas.FABRICA')),
                ('Pedidofk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabricas.Pedidos_Fabrica')),
            ],
        ),
    ]