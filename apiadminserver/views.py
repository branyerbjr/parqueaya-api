from django.shortcuts import render
from  rest_framework import viewsets
from .serializers import AdminservSerializer
from .models import Adminserv

# Create your views here.
class AdminservView(viewsets.ModelViewSet):
    serializer_class = AdminservSerializer
    queryset = Adminserv.objects.all()