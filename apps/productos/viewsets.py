from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewset(viewsets.ModelViewSet):

    model = Producto
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
