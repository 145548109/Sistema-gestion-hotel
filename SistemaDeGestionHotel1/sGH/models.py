from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre





