# Generated by Django 2.2 on 2020-05-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0007_auto_20200527_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Total',
            field=models.FloatField(),
        ),
    ]