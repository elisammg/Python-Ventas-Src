from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('new/', CreateFabrica.as_view(), name='newfabrica'),
    path('listado/', views.ListaFabricas, name='listafabricas'),
    path('listado/<pk>/updatecl', FabricasUpdate.as_view()), 
    path('listado/<pk>/deletecl', FabricaDelete.as_view()),



    path('crearpedido', views.CrearPedido, name='crearpedido'),
    path('detallepedido', views.CrearDetallePedido, name='detallepedido'),

    path('recibirpedido', views.pedidosapi, name='recibirpedido'),

    path('listado/<pk>/agregar', views.guardarpedido, name='guardarpedido'),

]