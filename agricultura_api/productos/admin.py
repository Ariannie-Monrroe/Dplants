from django.contrib import admin
from productos.models import Producto

admin.site.register(Producto)

producto1 = Producto(nombre="Macetero1", descripcion="macetero1", precio=15.000)
producto1.save()

producto2 = Producto(nombre="Macetero2", descripcion="macetero2", precio=16.000)
producto2.save()

producto3 = Producto(nombre="Macetero2", descripcion="macetero3", precio=17.000)
producto3.save()

producto4 = Producto(nombre="Planta1", descripcion="Planta1", precio=5.000)
producto4.save()

producto5 = Producto(nombre="Planta2", descripcion="Planta2", precio=6.000)
producto5.save()

producto6 = Producto(nombre="Planta3", descripcion="Planta3", precio=7.000)
producto6.save()

producto7 = Producto(nombre="PlantCare1", descripcion="Fertilizante1", precio=12.000)
producto7.save()

producto8 = Producto(nombre="PlantCare2", descripcion="Fertilizante2", precio=13.000)
producto8.save()

producto9 = Producto(nombre="PlantCare3", descripcion="Fertilizante3", precio=14.000)
producto9.save()


# Register your models here.
