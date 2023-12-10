import paho.mqtt.client as mqtt
from .serializer import *
from django.conf import settings
from .models import Servo
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class ServoListCreateView(generics.ListCreateAPIView):
    queryset = Servo.objects.all()
    serializer_class = ServoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {**serializer.data, 'ok': 202},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        instance = serializer.save()
        self.publish_to_broker(instance)

    def publish_to_broker(self, rele_instance):
        client = mqtt.Client()
        client.username_pw_set(username=settings.BROKER_USERNAME, password=settings.BROKER_PASSWORD)
        client.connect(settings.BROKER_HOST, settings.BROKER_PORT, 60)

        topic = rele_instance.topico

        # Si el estado es True, enviar "on" al broker, de lo contrario, enviar "off"
        message = f"{'1' if rele_instance.status else '0'}"

        client.publish(topic, message)
        client.disconnect()


class ServoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servo.objects.all()
    serializer_class = ServoSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'ok': 202}, status=status.HTTP_202_ACCEPTED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Modificar la respuesta para devolver solo el estado actualizado
        response_data = {'status': serializer.data['status']}
        return Response(response_data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        instance = serializer.save()
        self.publish_to_broker(instance)

    def perform_destroy(self, instance):
        self.publish_to_broker(instance)
        instance.delete()

    def publish_to_broker(self, rele_instance):
        client = mqtt.Client()
        client.username_pw_set(username=settings.BROKER_USERNAME, password=settings.BROKER_PASSWORD)
        client.connect(settings.BROKER_HOST, settings.BROKER_PORT, 60)

        topic = rele_instance.topico

        # Si el estado es True, enviar "on" al broker, de lo contrario, enviar "off"
        message = f"{'1' if rele_instance.status else '0'}"

        client.publish(topic, message)
        client.disconnect()
