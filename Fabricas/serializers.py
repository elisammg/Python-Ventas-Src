from .models import *
from rest_framework import serializers


class FabricaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FABRICA
        fields = '__all__'


class PedidosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedidos_Fabrica
        fields = '__all__'


class DetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_Pedido
        fields = '__all__'