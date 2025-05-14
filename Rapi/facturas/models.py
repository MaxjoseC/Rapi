from django.db import models
from pedidos.models import Pedido

class Factura(models.Model):

    Pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='factura')
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Factura {self.numero_factura} - Pedido {self.Pedido.id}'
    
    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['-fecha_emision']