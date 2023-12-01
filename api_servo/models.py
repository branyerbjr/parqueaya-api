from django.db import models

# Create your models here.
class Servo(models.Model):
    modelo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    caracteristicas = models.CharField(max_length=200)
    topico = models.CharField(max_length=200)