from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializers
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ClienteFilter

# Creación de views.

class ClienteListcreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers


class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClienteFilter

