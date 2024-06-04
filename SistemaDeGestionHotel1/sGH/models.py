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
class TipoCliente(models.Choices):
    NIÑO = 'Niño'
    ADULTO = 'Adulto'
    ADULTOMAYOR = 'Adulto Mayor'

class Cliente(models.Model):
    persona = models.ForeignKey(Persona,
                                on_delete=models.CASCADE,
                                related_name='cliente_list')
    tipo = models.CharField(max_length=15,
                             choices=TipoCliente.choices,
                             default=TipoCliente.ADULTO)
    def __str__(self):
        return self.persona.nombre

class Personal(models.Model):
    persona = models.ForeignKey(Persona,
                                on_delete=models.CASCADE,
                                related_name='personal_list')
    cargo = models.CharField(max_length=100)
    def __str__(self):
        return self.persona.nombre
class cargo(models.Choices):
    RECEPCIONISTA = 'Recepcionista'
    CHEF = 'Chef'
    GUARDIA = 'Guardia'
    CONSERJE = 'Conserje'
    GUIA = 'Guia'

class Estado(models.Choices):
    RESERVADO = 'Reservado'
    ENPROCESO = 'En Proceso'
    CANCELADO = 'Cancelado'
class Reservacion(models.Model):
    cliente = models.ForeignKey(Cliente,
                                on_delete=models.CASCADE,
                                related_name='reservacion_list')
    personal = models.ForeignKey(Personal,
                                 on_delete=models.CASCADE,
                                 related_name='reservacion_list')
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    def __str__(self):
        return self.cliente.persona.nombre




