from rest_framework import serializers
from .models import Admin, Usuario


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'provider_id', 'provider_specific_uid', 'nombres', 'apellidos', 'dni', 'telefono', 'correo', 'photo_url', 'password']


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'provider_id', 'provider_specific_uid', 'nombres', 'apellidos', 'dni', 'telefono', 'correo', 'photo_url', 'password']

    def create(self, validated_data):
        # Cambiar de create_user a create para evitar la encriptación automática
        user = Usuario.objects.create(**validated_data)
        return user
    

class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        correo = data.get('correo')
        password = data.get('password')

        if not correo or not password:
            raise serializers.ValidationError('Correo y contraseña son requeridos')

        return data


