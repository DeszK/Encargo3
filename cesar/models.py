from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpg')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'