from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets

# Item Views
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # Define any additional methods or customizations here if needed