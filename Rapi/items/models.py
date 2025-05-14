from django.db import models

# Creación de modelo item.

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.nombre.replace(" ", "-").lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['nombre']
