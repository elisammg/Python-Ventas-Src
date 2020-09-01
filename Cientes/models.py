from django.utils import timezone
from django.utils.timezone import datetime
from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.



class Tipo(models.Model):
	TIPO = (
			('mayorista', 'Mayorista'),
			('taller', 'Taller'),
		)
	ID_TIPO = models.AutoField(primary_key=True)
	nombre = models.CharField(choices = TIPO, max_length = 50)
	Descuento = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	

	def __str__(self):
		return self.nombre





class Clientes (models.Model):
	ESTADO = (
			('Activo', 'Activo'),
			('Inactivo', 'Inactivo'),
		)
	ID_CLIENTE = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	nit = models.PositiveIntegerField(unique=True)
	email = models.CharField(max_length=60)
	telefono = models.PositiveIntegerField()
	patente = models.ImageField(upload_to='images/')
	TIPO_ID = models.ForeignKey(Tipo, on_delete=models.CASCADE)	
	fecha_inicio = models.DateField(auto_now_add = False, default = '2020-01-01')
	fecha_fin = models.DateField(auto_now_add = False, default = '2020-01-01')
	estado = models.CharField(choices = ESTADO, max_length = 50, default = 'Activo')

	def __str__(self):
		return self.nombre
