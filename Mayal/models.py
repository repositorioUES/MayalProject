from unicodedata import category
from django.db import models

# Create your models here.

# ---CATEGORIA -------------------------------------------------------------------
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombreCat = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombreCat
#FIN CATEGORIA

# ---SUB-CATEGORIA -------------------------------------------------------------------
class Subcategoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombreSub = models.CharField(max_length = 100)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreCat
#FIN SUB-CATEGORIA

# ---SUB-CATEGORIA -------------------------------------------------------------------
class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    foto = models.ImageField(upload_to='Galeria')
    nombreProd = models.CharField(max_length=250)
    coleccion = models.CharField(max_length=250)
    material = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits = 5, decimal_places= 2)

    categoria = models.ForeignKey('Categoria', on_delete = models.SET_NULL, null=True)
    subCategoria = models.ForeignKey('Subcategoria', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.nombreServicio