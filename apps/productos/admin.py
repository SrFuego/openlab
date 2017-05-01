from django.contrib import admin

from .models import Producto, Seccion, Carrito, TipoUsuario


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'descripcion',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Seccion)
admin.site.register(Carrito)
admin.site.register(TipoUsuario)
