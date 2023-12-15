from rest_framework import serializers
from .models import Admin, Usuario


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'provider_id', 'provider_specific_uid', 'nombres', 'apellidos', 'dni', 'telefono', 'correo', 'fecha_registro', 'photo_url']


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'provider_id', 'provider_specific_uid', 'nombres', 'apellidos', 'dni', 'correo', 'photo_url', 'password']

    def create(self, validated_data):
        validated_data['password'] = validated_data.pop('password', None)
        user = Usuario.objects.create_user(**validated_data)
        return user



class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

