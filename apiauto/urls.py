from django.urls import path
from .views import AutoListCreateView, AutoDetailView

urlpatterns = [
    path('auto/', AutoListCreateView.as_view(), name='auto-list-create'),
    path('auto/<int:pk>/', AutoDetailView.as_view(), name='auto-detail'),
]
