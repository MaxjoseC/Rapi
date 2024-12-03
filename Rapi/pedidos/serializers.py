from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def validate_estado(self, value):
        if value not in ['pendiente', 'completado', 'cancelado']:
            raise serializers.ValidationError("Estado inválido")
        return value