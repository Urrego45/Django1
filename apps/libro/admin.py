from django.contrib import admin

from apps import libro

from .models import Libro, Categoria
# Register your models here.

admin.site.register(Libro)
admin.site.register(Categoria)