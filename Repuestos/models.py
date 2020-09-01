from django.db import models
from Fabricas.models import *

# Create your models here.

class VEHICULO(models.Model):
    id_Vehiculo = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=200)
    Linea = models.CharField(max_length=200)
    Anio = models.CharField(max_length=200)
    Codigo_Universal = models.CharField(unique = True, max_length=200)


    def __str__(self):
        return 'Vehiculo: ' + self.Marca





class REPUESTOS(models.Model):
    Codigo_Repuesto = models.AutoField(primary_key=True)
    #Precio_De_Lista = models.FloatField(default=0.00)
    Modelo_De_Parte = models.IntegerField(default=0)
    Nombre = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200, default = 0)
    Vehiculo_Compatible = models.ForeignKey(VEHICULO, on_delete=models.CASCADE, default=0)
    Stock = models.IntegerField(default=0)
    Fabrica = models.ForeignKey(FABRICA, on_delete=models.CASCADE, default=0)
    Precio_Fabricante = models.FloatField(default=0.00)
    Precio_Venta= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.Nombre

    def preciofinal (self):
        self.Precio_Venta = (self.Precio_Fabricante + (self.Precio_Fabricante * 0.15) + (self.Precio_Fabricante*0.3) + (self.Precio_Fabricante*0.05) + (self.Precio_Fabricante*0.4)) + (self.Precio_Fabricante*0.12)
        return self.precio