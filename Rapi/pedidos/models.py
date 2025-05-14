from django.db import models
from clientes.models import Cliente

# models de pedidos
class Pedido (models.Model):
    PENDIENTE = 1
    COMPLETADO = 2
    CANCELADO = 3
    ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (COMPLETADO, 'Completado'),
        (CANCELADO, 'Cancelado'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    items = models.ManyToManyField('items.Item', related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(choices=ESTADOS, default=PENDIENTE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nombre}'
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']