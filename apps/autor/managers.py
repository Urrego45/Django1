from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para el modelo autor """
    
    def buscar_autor(self, kword):

        resultado = self.filter(
            nombre__icontains = kword
        )
        
        return resultado

    def buscar_autor2(self, kword):

        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains=kword)
        )
        
        return resultado

    def buscar_autor3(self, kword):

        resultado = self.filter(
            nombre__icontains = kword
        ).exclude(
            Q(edad__icontains=60) | Q(edad__icontains=45)
        )
        
        return resultado
    
    def buscar_autor4(self, kword):

        resultado = self.filter(
            edad__gt=30,
            edad__lt=70
        ).order_by('apellidos', 'nombre', 'id')
        
        return resultado