from django.db import models
from apiadmin.models import Usuario
from servicios.models import Transaccion


# Create your models here.
class Auto(models.Model):
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autos')
    placa = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    
    transaccion = models.OneToOneField(Transaccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.placa