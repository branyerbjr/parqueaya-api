# api-services/models.py
from django.db import models


class TelegramSettings(models.Model):
    token = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default="Default Name")
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)


class WhatsAppSettings(models.Model):
    id_instance = models.CharField(max_length=255)
    api_token_instance = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="Default Name")
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
