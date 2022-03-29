from django.db import models
from django.db.models.signals import post_save

# apps tercero
from PIL import Image



#
from distutils.command.upload import upload

# from local apps

from apps.autor.models import Autor
from .managers import CategoriaManager, LibroManager

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    
    objects = CategoriaManager()
    
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre
    

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('Titulo', max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True)
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default= 0)

    objects = LibroManager()
    
    def __str__(self):
        return str(self.id) + ' - ' + self.titulo + ' - ' + str(self.autores) + ' - ' + self.titulo + ' - ' + str(self.fecha) + ' - ' + str(self.visitas) + ' - ' + str(self.stok)



def optimize_image(sender, instance, **kwargs):
    print(" ============= ")
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)
    
    
post_save.connect(optimize_image, sender=Libro)