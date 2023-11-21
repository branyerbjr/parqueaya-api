from rest_framework import serializers
from .models import Adminserv

class AdminservSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminserv
        exclude = ['contraseña']