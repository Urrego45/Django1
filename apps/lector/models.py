from django.db import models


# from local apps

from apps.libro.models import Libro

# Create your models here.

class Lector(models.Model):
    nombres = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=20)
    edad = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nombres + ' - ' + self.apellidos + ' - ' + self.nacionalidad + ' - ' + str(self.edad)


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    devuelto = models.BooleanField()
    
    def save(self, *args, **kwargs):
        print('===============')
        self.libro.stok = self.libro.stok - 1
        self.libro.save()
        
        super(Prestamo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.libro.titulo