from rest_framework import generics
from .models import Parqueo
from .serializers import ParqueoSerializer

class ParqueoListCreateView(generics.ListCreateAPIView):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer

class ParqueoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
