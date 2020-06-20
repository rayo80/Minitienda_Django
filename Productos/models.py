from django.db import models
from Usuarios.models import usuario
from autoslug import AutoSlugField

from datetime import datetime


# Create your models here.

class categoria(models.Model):
  
    #  Define fields here
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=('titulo'), unique=True )


    class Meta:
        

        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.titulo
        

class subcategoria(models.Model):
    
    #  Define fields here
    id = models.AutoField(primary_key=True)
    categoria_id = models.ForeignKey('categoria',related_name='products',on_delete=models.CASCADE)

    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=('titulo'), unique=True )
    

    class Meta:
        

        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'

    def __str__(self):
        return self.titulo

class producto(models.Model):

    # Define fields here
    id = models.AutoField(primary_key=True)
    categoria_id = models.ForeignKey('categoria',related_name='producto',on_delete=models.CASCADE)
    sub_categoria_id = models.ForeignKey('subcategoria',related_name='sub_categoria',on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(usuario,related_name='usuario_producto',on_delete=models.CASCADE)

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    precio = models.DecimalField(max_digits=12, decimal_places=0)
    foto = models.ImageField( upload_to='producto/%Y/%m/', null=True, blank=True)
    slug = AutoSlugField(populate_from=('titulo'), unique=True )


    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering=['titulo']

    def __str__(self):
        return self.titulo
