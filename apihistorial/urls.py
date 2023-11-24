from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistorialListCreateView, HistorialDetailView

router = DefaultRouter()
router.register(r'historial', HistorialListCreateView, basename='historial')

urlpatterns = [
    path('', include(router.urls)),
    path('historial/<int:pk>/', HistorialDetailView.as_view(), name='historial-detail'),
]
