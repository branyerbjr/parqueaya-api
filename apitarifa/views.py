from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Tarifa
from .serializers import TarifaSerializer
import datetime

class CalcularTarifa(APIView):
    def cost(self, request):
        tiempo_estacionado = request.data.get('tiempo_estacionado')

# Create your views here.
