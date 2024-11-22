from django.urls import path
from .views import ClienteListcreate, ClienteRetrieveUpdateDestroy

urlpatterns = [
    path('clientes/', ClienteListcreate.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'), 
    ]
    
    