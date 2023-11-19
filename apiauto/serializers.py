<<<<<<< HEAD
from rest_framework import serializers
from .models import Auto
from apiuser.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
=======
from rest_framework import serializers
from .models import Auto
from apiuser.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
        fields = '__all__'