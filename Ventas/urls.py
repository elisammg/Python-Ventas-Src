from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('newuser', views.newuser, name='newuser'),
	path('', views.vista_sesion, name='login'),
	path('administrador', views.vista_administrador, name='administrador'),
	path('salir',views.logout, name='salir'),

    path('vendedor', views.vista_vendedor, name='vendedor'),  
#    path('vender', views.vista_Ventas, name='vender'),
	path('vender', views.newventa, name='vender'),


    path('detalle', views.listardetalle, name='detalle'),
    path('individual', views.individual, name='individual'),
    path('registrado', views.registrado, name='registrado'),
    path('credito', views.credito, name='credito'),
    path('futuro', views.futuro, name='futuro'),


    path('prueba', views.prueba, name='prueba'),
]