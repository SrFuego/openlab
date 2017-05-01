from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):

    model = Producto
    fields = ('nombre', 'precio', 'descripcion', 'cantidad', 'seccion',)
