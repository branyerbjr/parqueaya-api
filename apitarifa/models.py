from django.db import models

# Create your models here.
class Tarifa(models.Model):
    nombre = models.CharField(max_length=255)
    costo_por_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre