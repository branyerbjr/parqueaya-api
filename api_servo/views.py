#from rest_framework import viewsets
#from rest_framework.decorators import action
#from rest_framework.response import Response
#from .models import Servo
#from .serializers import ServoSerializer
#import paho.mqtt.client as mqtt

#class ServoViewSet(viewsets.ModelViewSet):
#    queryset = Servo.objects.all()
#    serializer_class = ServoSerializer

#    @action(detail=True, methods=['post'])
#    def control_servo(self, request, pk=None):
#        angle = request.data.get('angle', 0)
#        servo = self.get_object()

        # Enviar el comando MQTT al servidor para controlar el servo
#        mqtt_client = mqtt.Client()
#        mqtt_client.username_pw_set(username="admin", password="@Parqueaya2023")
#        mqtt_client.connect("34.23.25.139", 1883, 60)
#        topic = servo.topico  # Asume que el campo 'topico' en el modelo Servo contiene el nombre del tópico MQTT
#        mqtt_client.publish(topic, angle)
#        mqtt_client.disconnect()

        # Actualizar el estado del servo en la base de datos
#        servo.estado = f'Moved to angle: {angle}'
#        servo.save()

#        return Response({'message': f'Servo {servo.modelo} moved to angle: {angle}'})
