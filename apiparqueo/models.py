from django.db import models

# Create your models here.
class Parqueo(models.Model): 
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    capacidad = models.PositiveIntegerField()
    tarifa_hora = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
