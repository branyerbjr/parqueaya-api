# views.py

from rest_framework import generics
from .models import Usuario, MetodoPago, Transaccion, Devolucion, RegistroPagos, Tarifa
from .serializers import MetodoPagoSerializer, TransaccionSerializer, DevolucionSerializer, RegistroPagosSerializer, TarifaSerializer
from apiuser.serializers import UsuarioSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MetodoPagoListCreateView(generics.ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class TransaccionListCreateView(generics.ListCreateAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class TransaccionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class DevolucionListCreateView(generics.ListCreateAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

class DevolucionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

class RegistroPagosListCreateView(generics.ListCreateAPIView):
    queryset = RegistroPagos.objects.all()
    serializer_class = RegistroPagosSerializer

class RegistroPagosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroPagos.objects.all()
    serializer_class = RegistroPagosSerializer

class TarifaListCreateView(generics.ListCreateAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

class TarifaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer
