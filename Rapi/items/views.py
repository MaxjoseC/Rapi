from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# Item Views
class ListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
