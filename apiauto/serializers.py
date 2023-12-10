from rest_framework import serializers
from .models import Auto
from apiadmin.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'
