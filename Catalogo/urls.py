from django.urls import include, path
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'vehiculo', views.VehiculosViewSet)


urlpatterns = [

    path('clientes/', login_required(views.product_list), name='product_list'),
    path('fabrica/list', login_required(views.fabric_list), name='fabric_list'),
    path('vehiculo/list', login_required(views.vehiculo_list), name='vehiculo_list'),
    path('product/new/', login_required(views.product_new), name='product_new'),
    path('fabric/new/', login_required(views.fabric_new), name='fabric_new'),
    path('vehiculo/new/', login_required(views.vehiculo_new), name='vehiculo_new'),
    path('product/<int:producto_id>/', login_required(views.product_detail), name='product_detail'),
    path('compatibilidad/', login_required(views.compatible_list), name='compatibilidad_list'),
    path('compatibilidad/new', login_required(views.nueva_compatibilidad), name='comp_new'),
    path('rt', include(router.urls)),
]
