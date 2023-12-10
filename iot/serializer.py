from rest_framework import serializers
from .models import *


class ServoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servo
        fields = ['id', 'nombre', 'topico', 'status']
