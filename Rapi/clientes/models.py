from django.db import models

# Modelo de cliente.
class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    sector = models.CharField(max_length=100)
    descuentoBool = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
