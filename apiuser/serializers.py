from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='contrasena', read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    contrasena = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user


class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(style={'input_type': 'password'})