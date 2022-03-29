from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libro/', views.ListLibros.as_view(), name="libros"),
    path('libro2/', views.ListLibros2.as_view(), name="libros2"),
    path('libro_detalle/<pk>/', views.LibroDetailView.as_view(), name="libro_detalle"),
]
