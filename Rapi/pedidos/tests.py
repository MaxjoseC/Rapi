from django.test import TestCase
from clientes.models import Cliente
from .models import Pedido

class PedidoModelTest(TestCase):
    def test_crear_pedido(self):
        cliente = Cliente.objects.create(
            nombre="Juan Pérez",
            telefono="+123456789",
            direccion="Calle Falsa 123",
            descuentoBool=True
        )

        pedido = Pedido.objects.create(
            cliente=cliente, estado=0, total=100.00  # Usando número en lugar de 'pendiente'
        )

        self.assertEqual(pedido.estado, 0)  # Comparación con el valor numérico esperado