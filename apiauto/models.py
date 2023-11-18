from django.db import models
from apiuser.models import Usuario

# Create your models here.
class Auto(models.Model):
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    placa = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)

    def __str__(self):
        return self.placa