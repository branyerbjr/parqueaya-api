# views.py

from rest_framework import generics
from .models import Usuario, MetodoPago, Transaccion, Devolucion, RegistroPagos, Tarifa
from .serializers import MetodoPagoSerializer, TransaccionSerializer, DevolucionSerializer, RegistroPagosSerializer, \
    TarifaSerializer
from apiadmin.serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from paypalrestsdk import Payment, configure


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

class PayPalPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        # Configura las credenciales de PayPal (reemplaza 'YOUR_CLIENT_ID' y 'YOUR_CLIENT_SECRET' con tus propias credenciales)
        configure({
            "mode": "sandbox",  # Cambia a "live" en producción
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
        })

        # Lógica para crear un pago de PayPal y obtener el enlace de aprobación
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": "URL_DE_RETORNO",
                "cancel_url": "URL_DE_CANCELACION",
            },
            "transactions": [{
                "amount": {
                    "total": "TOTAL_DEL_PAGO",
                    "currency": "USD",  # Cambia a la moneda deseada
                },
                "description": "DESCRIPCION_DEL_PAGO",
            }],
        })

        if payment.create():
            approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
            return Response({"approval_url": approval_url})
        else:
            return Response({"error": "No se pudo crear el pago de PayPal"}, status=500)