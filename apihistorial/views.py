from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Historial
from .serializers import HistorialSerializer

class HistorialListCreateView(generics.ListCreateAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class HistorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
    permission_classes = [IsAuthenticated]
