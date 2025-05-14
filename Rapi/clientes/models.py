from django.db import models
from django.core.validators import RegexValidator

# Modelo de cliente.
class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=15, validators=[RegexValidator(regex=r'^\d{9,15}$', message='El número de teléfono debe de tener entre 9 y 15 dígitos.')]
    )
    direccion = models.CharField(max_length=200, default='Sin dirección')
    email = models.EmailField(max_length=100, default='Sin email')
    descuentoBool = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']