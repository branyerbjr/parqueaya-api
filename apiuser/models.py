<<<<<<< HEAD
from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    @property
    def usuario(self):
        primer_nombre = self.nombres.split()[0] if self.nombres else ""
        primer_apellido = self.apellidos.split()[0] if self.apellidos else ""
        return f"{primer_nombre}_{primer_apellido}"

    def __str__(self):
=======
from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    @property
    def usuario(self):
        primer_nombre = self.nombres.split()[0] if self.nombres else ""
        primer_apellido = self.apellidos.split()[0] if self.apellidos else ""
        return f"{primer_nombre}_{primer_apellido}"

    def __str__(self):
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
        return f"{self.usuario} - {self.correo}"