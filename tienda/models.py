from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models



# Create your models here.
class CategoriaProducto(models.Model):

    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaproducto'
        verbose_name_plural='categoriasproducto'

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    categorias=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    disponibilidad=models.BooleanField(default=True)
    precio=models.FloatField()


    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre



