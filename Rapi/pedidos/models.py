from django.db import models
from clientes.models import Cliente

# models de pedidos
class Pedido (models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)
