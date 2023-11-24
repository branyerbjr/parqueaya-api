from django.db import models
from apiuser.models import Usuario

# Create your models here.

class MetodoPago(models.Model):
    tipo_metodo_pago = models.CharField(max_length=255)
    datos_metodo_pago = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Transaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)


class Devolucion(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    motivo = models.TextField()


class RegistroPagos(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    estado_pago = models.CharField(max_length=255)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro de Pagos - {self.fecha_pago}"

class Tarifa(models.Model):
    tipo_tarifa = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)