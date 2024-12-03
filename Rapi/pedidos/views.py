from rest_framework import generics
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
