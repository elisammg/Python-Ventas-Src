from django.db import models
from Fabricas.models import *
from Cientes.models import *
from Repuestos.models import *

# Create your models here.


class Usuario(models.Model):
    ROL = (
            ('Administrador', 'Administrador'),
            ('Vendedor', 'Vendedor'),
        )
    ID_USUARIO = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length = 100)  
    Usuario =  models.CharField(max_length = 100) 
    Password =  models.CharField(max_length = 100) 
    Rol = models.CharField(choices = ROL, max_length = 100)

    def __str__(self):
        return 'Usuario: ' + self.Usuario



#Abrir orden de venta
class Ventas(models.Model):
    TIPO = (
            ('Individual', 'Individual'),
            ('Registrado', 'Registrado'),            
            ('Credito', 'Credito'),
            ('Futuro', 'Futuro'),
        )
    Codigo_Venta = models.AutoField(primary_key=True)
    Tipo_Venta = models.CharField(choices = TIPO, max_length = 100)
    #Fabricante = models.ForeignKey(FABRICA, on_delete=models.CASCADE)    
    Vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Codigo_Venta)




class FACTURA(models.Model):
    Numero_Factura = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, blank = True, null = True)
    Total = models.FloatField()
    Estado = models.CharField(max_length=200)
    Venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, default=0)
    Nombre_cliente = models.CharField(max_length=200, null = True)
    Nit = models.PositiveIntegerField(null = True)


    def __str__(self):
        return str(self.Numero_Factura)




class Detalle_Venta(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, default=0)
    Repuesto  = models.ForeignKey(REPUESTOS, on_delete=models.CASCADE, default=0)
    Cantidad = models.IntegerField(default=0)
    Sub_Total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    #Factura = models.ForeignKey(FACTURA, on_delete=models.CASCADE, default=0)

    
    def __str__(self):
        return str(self.Codigo)


    def valor_subtotal (self):
        self.Sub_Total = self.Cantidad * self.Repuesto.Precio_Venta
        return self.Sub_Total
