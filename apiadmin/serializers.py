from rest_framework import serializers
from .models import Admin, Usuario


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'telefono', 'nombres', 'apellidos', 'correo', 'usuario', 'dni', 'correo', 'photo_url')
