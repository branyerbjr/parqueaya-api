# views.py en tu aplicación de autos
from rest_framework import generics
from .models import Auto
from .serializers import AutoSerializer

class AutoListCreateView(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class AutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

