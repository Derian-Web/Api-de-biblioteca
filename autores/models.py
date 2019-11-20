from django.db import models
from editorial.models import Editorial
from libros.models import Libro


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    libros = models.ManyToManyField(Libro)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def ___str__(self):
        return self.nombre

