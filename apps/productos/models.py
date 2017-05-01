from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Seccion(models.Model):

    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    cantidad = models.PositiveSmallIntegerField()
    descripcion = models.TextField()
    nombre = models.CharField(max_length=100)
    precio = models.PositiveSmallIntegerField()
    precio_oferta = models.PositiveSmallIntegerField()
    seccion = models.ForeignKey('Seccion', blank=True, null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre


class Carrito(models.Model):

    productos = models.ManyToManyField('Producto')
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return super(Carrito, self).__str__()


class TipoUsuario(models.Model):

    TIPO_CHOICES = (
        ('vendedor', 'Vendedor'),
        ('comprador_normal', 'Comprador Basico'),
        ('comprador_premium', 'Comprador Premium'),
    )

    tipo = models.CharField(choices=TIPO_CHOICES, max_length=10)
    usuario = models.ForeignKey(User)
    descuento = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipo Usuarios"

    def __str__(self):
        return self.tipo
