from django.db import models
from apiuser.models import Usuario

# Create your models here.
class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - ${self.monto} - {self.fecha_pago}'