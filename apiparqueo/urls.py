from django.urls import path
from .views import ParqueoListCreateView, ParqueoRetrieveUpdateDestroyView

urlpatterns = [
    path('parqueos/', ParqueoListCreateView.as_view(), name='parqueo-list-create'),
    path('parqueos/<int:pk>/', ParqueoRetrieveUpdateDestroyView.as_view(), name='parqueo-detail'),
]
