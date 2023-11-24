from rest_framework import serializers
from .models import Historial
from apiuser.serializers import UsuarioSerializer  

class HistorialSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()  

    class Meta:
        model = Historial
        fields = ('id', 'usuario', 'monto', 'fecha_pago')
        read_only_fields = ('id', 'fecha_pago')