from django.urls import path
from . import views
from .views import *

urlpatterns = [
	#path('newcliente', views.newcliente, name='newcliente'),

    path('new/', CreateCliente.as_view(), name='newcliente'),
    path('listado/', views.ListaClientes, name='listaclientes'),
    path('listado/<pk>/updatecl', ClientesUpdate.as_view()), 
    path('listado/<pk>/deletecl', ClienteDelete.as_view()),


    path('cursor', views.Modificar_Suscripcion, name='cursor'),

]