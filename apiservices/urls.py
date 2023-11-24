# apiservices/urls.py
from django.urls import path
from apiservices.views import TelegramSettingsView, WhatsAppSettingsView, send_whatsapp_message

urlpatterns = [
    path('telegram-settings/', TelegramSettingsView.as_view(), name='telegram-settings'),
    path('whatsapp-settings/', WhatsAppSettingsView.as_view(), name='whatsapp-settings'),
    path('send-whatsapp-message/', send_whatsapp_message, name='send-whatsapp-message'),
]
