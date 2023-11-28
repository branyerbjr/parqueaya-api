# apiservices/models.py
from django.db import models


class TelegramSettings(models.Model):
    token = models.CharField(max_length=255, unique=True)


class WhatsAppSettings(models.Model):
    id_instance = models.CharField(max_length=255)
    api_token_instance = models.CharField(max_length=255)
