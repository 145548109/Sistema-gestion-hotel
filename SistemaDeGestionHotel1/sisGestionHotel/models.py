from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)

class Cliente(Persona):
    tipo = models.CharField(max_length=100)

class Personal(Persona):
    cargo = models.CharField(max_length=100)

class Habitacion(models.Model):
    numero = models.IntegerField(unique=True)
    categoria = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)

class Reservacion(models.Model):
    nro
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=100)  # Usar Enum Estado

class Factura(models.Model):
    reservacion = models.OneToOneField(Reservacion, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos como detalles, fecha de emisión, etc.

# Definir Enums
class TipoCliente(models.TextChoices):
    NIÑO = 'Niño'
    ADULTO = 'Adulto'
    ADULTO_MAYOR = 'Adulto Mayor'

class Estado(models.TextChoices):
    PENDIENTE = 'Pendiente'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'

class Disponibilidad(models.TextChoices):
    DISPONIBLE = 'Disponible'
    OCUPADA = 'Ocupada'