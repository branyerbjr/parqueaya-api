<<<<<<< HEAD
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
=======
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
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
