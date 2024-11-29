from django_filters import rest_framework as filters
from .models import Cliente

#filtrar por numero o nombre
class ClienteFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    telefono = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono'] 