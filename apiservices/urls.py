# apiservices/urls.py
from django.urls import path
from .views import (
    TelegramSettingsView, TelegramSettingsListView,
    WhatsAppSettingsView, WhatsAppSettingsListView,
    send_whatsapp_message, send_whatsapp_file
)

urlpatterns = [
    path('telegram/', TelegramSettingsView.as_view(), name='telegram-settings'),
    path('telegram/list/', TelegramSettingsListView.as_view(), name='telegram-settings-list'),
    path('whatsapp/', WhatsAppSettingsView.as_view(), name='whatsapp-settings'),
    path('whatsapp/list/', WhatsAppSettingsListView.as_view(), name='whatsapp-settings-list'),
    path('whatsapp/send-message/<str:id_instance>/', send_whatsapp_message, name='send-whatsapp-message'),
    path('whatsapp/send-file/<str:id_instance>/', send_whatsapp_file, name='send-whatsapp-file'),
]
