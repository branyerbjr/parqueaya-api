from django.db import models


class Servo(models.Model):
    nombre = models.CharField(max_length=255)
    topico = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
