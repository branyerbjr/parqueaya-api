<<<<<<< HEAD
from django.db import models

class Admin(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
=======
from django.db import models

class Admin(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
        return self.usuario