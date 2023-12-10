from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    provider_id = models.CharField(max_length=255)
    provider_specific_uid = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=8)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255, verbose_name='contraseña')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField()

    def save(self, *args, **kwargs):
        # Antes de guardar el modelo, encripta la contraseña si es nueva o modificada
        if self._state.adding or 'contrasena' in self.get_dirty_fields():
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    @property
    def usuario(self):
        primer_nombre = self.nombres.split()[0] if self.nombres else ""
        primer_apellido = self.apellidos.split()[0] if self.apellidos else ""
        return f"{primer_nombre}_{primer_apellido}"

    def __str__(self):
        return f"{self.usuario} - {self.correo}"


class Admin(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario
