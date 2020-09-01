"""ProyectoDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static # new
from rest_framework import routers
from Fabricas import views



router = routers.DefaultRouter()
router.register(r'fabricas', views.FabricaViewSet)
router.register(r'pedidos', views.PedidosViewSet)
router.register(r'detalle', views.DetalleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('Cientes.urls')),
    path('fabricas/', include('Fabricas.urls')),
    path('repuestos/', include('Repuestos.urls')),
    path('', include('Ventas.urls')),
    path('rest', include(router.urls)),
    path('api-rest/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
