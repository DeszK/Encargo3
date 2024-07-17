from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpg')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

opciones_contacto = [
    [0, "Reclamo"],
    [1, "Trabajo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=69)
    apellido = models.CharField(max_length=69)
    correo = models.EmailField()
    tipo_contacto = models.IntegerField(choices=opciones_contacto)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    