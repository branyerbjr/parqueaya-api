# serializers.py

from rest_framework import serializers
from .models import MetodoPago, Transaccion, Devolucion, RegistroPagos, Tarifa


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'

class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucion
        fields = '__all__'

class RegistroPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPagos
        fields = '__all__'

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'
