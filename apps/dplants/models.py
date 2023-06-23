from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=22)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.id_categoria, self.nombre_categoria)


class Producto(models.Model):
    
    sku = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=120)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Producto N° {0} - Stock {1} - Precio {2} - fecha {3}"
        return txt.format(self.sku, self.stock, self.precio, self.fecha)
    
class Vendido(models.Model):
    
    sku_vendido = models.CharField(primary_key=True,max_length=15)
    nombre_vendido = models.CharField(max_length=50)
    precio_vendido = models.IntegerField()
    stock_vendido = models.IntegerField()
    fecha_vendido = models.DateField(auto_now_add=True)
    descripcion_vendido = models.CharField(max_length=120)
    imagenUrl_vendido = models.ImageField(upload_to="imagenesProducto")
    categoriaId_vendido = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Producto N° {0} - Stock {1} - Precio {2} - fecha {3}"
        return txt.format(self.sku_vendido, self.stock_vendido, self.precio_vendido, self.fecha_vendido)

class Usuario(models.Model):
    
    id= models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)  
    
    def __str__(self):
        txt= "Id {0} - Correo {1} - Usuario {2} - Contraseña {3}"
        return txt.format(self.id, self.correo, self.usuario, self.contraseña) 
