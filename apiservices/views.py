from rest_framework import generics
from .models import TelegramSettings, WhatsAppSettings
from .serializers import TelegramSettingsSerializer, WhatsAppSettingsSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


class TelegramSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = TelegramSettingsSerializer

    def get_object(self):
        # Solo hay un registro, por lo que siempre devolvemos el primer objeto
        return TelegramSettings.objects.first()


class WhatsAppSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = WhatsAppSettingsSerializer

    def get_object(self):
        # Solo hay un registro, por lo que siempre devolvemos el primer objeto
        return WhatsAppSettings.objects.first()


@csrf_exempt
def send_whatsapp_message(request):
    if request.method == 'POST':
        url = "https://api.greenapi.com/waInstance{{idInstance}}/sendMessage/{{apiTokenInstance}}"
        chat_id = request.POST.get('chatId')
        message = request.POST.get('message')

        payload = {
            'chatId': chat_id,
            'message': message
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        return JsonResponse({'status_code': response.status_code, 'response_text': response.text})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
