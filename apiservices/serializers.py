# apiservices/serializers.py
from rest_framework import serializers
from .models import TelegramSettings, WhatsAppSettings

class TelegramSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramSettings
        fields = '__all__'

class WhatsAppSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsAppSettings
        fields = '__all__'
