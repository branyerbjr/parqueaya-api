from rest_framework import serializers
from .models import Admin, Usuario


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'contraseña', 'usuario', 'nombres', 'apellidos']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
