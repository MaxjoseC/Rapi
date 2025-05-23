from rest_framework import viewsets
from clientes.models import Cliente
from clientes.serializers import ClienteSerializers

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers