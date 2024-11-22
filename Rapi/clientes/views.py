from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializers

# Creación de views.

class ClienteListcreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryet = Cliente.objects.all()
    serializer_class = ClienteSerializers


