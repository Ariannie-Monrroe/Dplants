from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Categoria)
admin.site.register(models.Producto)
admin.site.register(models.Vendido)
admin.site.register(models.Usuario)
