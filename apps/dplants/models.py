from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']
        

class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Informacion del producto')
    avaible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']   

class Usuario(models.Model):
    
    id= models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)  
    
    def __str__(self):
        txt= "Id {0} - Correo {1} - Usuario {2} - Contraseña {3}"
        return txt.format(self.id, self.correo, self.usuario, self.contraseña) 