from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contrasena=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(correo)
        user = self.model(correo=email, **extra_fields)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        return self.create_user(correo, contrasena, **extra_fields)

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    provider_id = models.CharField(max_length=255)
    provider_specific_uid = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=8)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField()

    @property
    def usuario(self):
        primer_nombre = self.nombres.split()[0] if self.nombres else ""
        primer_apellido = self.apellidos.split()[0] if self.apellidos else ""
        return f"{primer_nombre}_{primer_apellido}"

    def __str__(self):
        return f"{self.usuario} - {self.correo}"