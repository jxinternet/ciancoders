from django.db import models
from django.contrib.auth.models import User

class CianCoders(models.Model):
    ordenes = models.CharField(max_length=500)
    ventas = models.TextField(blank=True)
    done = models.BooleanField(default=False)

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto')

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
