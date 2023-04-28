from rest_framework import serializers
from .models import Vendedor, Producto
from .models import CianCoders

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CianCoders
        fields = ['id', 'ordenes', 'ventas', 'done']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id', 'usuario', 'productos']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'vendedor']