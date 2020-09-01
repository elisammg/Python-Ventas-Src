from django.db import models

# Create your models here.

class FABRICA(models.Model):
    IP = models.CharField(max_length=200)
    Puerto= models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.IP + self.Puerto


class Pedidos_Fabrica(models.Model):
    ESTADO = (
            ('enviado', 'Enviado'),
            ('proceso', 'Proceso'),
            ('recibido', 'Recibido'),
        )    
    Codigo_Pedido = models.AutoField(primary_key=True)
    Codigo_Fabrica = models.ForeignKey(FABRICA, on_delete=models.CASCADE, null = True)
    Fecha_Pedido = models.DateField(auto_now_add = True)
    Fecha_Recepcion = models.DateField(auto_now_add = False, null = True)
    Total= models.FloatField(null = True)
    Estado = models.CharField(choices = ESTADO, max_length = 50, null = True)

    def __str__(self):
        return str(self.Codigo_Pedido)


class Detalle_Pedido(models.Model):   
    DetalleID = models.AutoField(primary_key=True) 
    Productos = models.CharField(max_length = 50)
    Cantidad = models.IntegerField(default=0)    
    Fabricante = models.ForeignKey(FABRICA, on_delete=models.CASCADE)    
    Sub_Total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    Pedidofk = models.ForeignKey(Pedidos_Fabrica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.DetalleID)




class Recepcion_Fabrica(models.Model):
    Codigo_RF  = models.AutoField(primary_key=True)
    Codigo_Pedido =  models.CharField(max_length=200, null = True)
    #Codigo_ProductoFab = models.CharField(max_length=200, null = True, blank = True)
    Precio_lista  = models.CharField(max_length=200, null = True)
    Numero_De_Parte = models.CharField(max_length=200, null = True)
    Nombre_Producto =  models.CharField(max_length=200, null = True)
    Fecha_Pedido = models.CharField(max_length=200, null = True)
    Fecha_Recepcion = models.CharField(max_length=200, null = True)
    Cantidad = models.CharField(max_length=200, null = True)
    Precio_Fabricante = models.CharField(max_length=200, null = True)
    Total = models.CharField(max_length=200, null = True)
    #Pedido_Fabrica  = models.ForeignKey(Pedidos_Fabrica, on_delete=models.CASCADE, default=0);
    Fabricante = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.Codigo_RF)



class Prueba(models.Model):
    idfk =  models.CharField(max_length=200)
    fecha_recibido =  models.CharField(max_length=200)
    fecha_entrega =  models.CharField(max_length=200)
    estado =  models.CharField(max_length=200)
    repuestos =  models.CharField(max_length=200)
    clientes =  models.CharField(max_length=200)
    precio_final =  models.CharField(max_length=200)
    cantidad =  models.CharField(max_length=200)

    def __str__(self):
        return str(self.idfk)

