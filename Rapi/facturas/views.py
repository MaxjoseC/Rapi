from django.shortcuts import render
from .models import Factura
from rest_framework import viewsets
from .serializers import FacturaSerializer
# Create your views here.
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    # Define any additional methods or customizations here if needed