from django.urls import path
from . import views
from .views import *

urlpatterns = [
	#path('newcliente', views.newcliente, name='newcliente'),

    path('new/', CreateRepuesto.as_view(), name='newrepuesto'),
    path('listado/', views.ListaRepuestos, name='listarepuestos'),
    path('listado/<pk>/updatecl', RepuestoUpdate.as_view()), 
    path('listado/<pk>/deletecl', RepuestoDelete.as_view()),

    #Vehiculos
    path('new/vehiculo', CreateVehiculo.as_view(), name='newvehiculo'),
    path('vehiculos/', views.ListaVehiculo, name='listavehiculos'),
    path('vehiculos/<pk>/updatecl', VehiculoUpdate.as_view()), 
    path('vehiculos/<pk>/deletecl', VehiculoDelete.as_view()),

]
