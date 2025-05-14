from rest_framework import generics
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework import viewsets

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer