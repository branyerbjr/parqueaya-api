from django.db import models


# Create your models here.
class Adminserv(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario
