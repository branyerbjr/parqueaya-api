<<<<<<< HEAD
from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'usuario', 'nombres', 'apellidos']
=======
from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'usuario', 'nombres', 'apellidos']
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
