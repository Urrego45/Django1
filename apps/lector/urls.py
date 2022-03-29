from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lector/', views.ListLector.as_view(), name="lectores"),
    path('prestamo/add/', views.AddPrestamo.as_view(), name="prestamo_add"),
    path('prestamo/multiple_add/', views.AddMultiplePrestamo.as_view(), name="prestamo_add_multiple"),
]
