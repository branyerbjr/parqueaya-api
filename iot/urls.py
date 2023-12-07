from django.urls import path
from . import views

urlpatterns = [
    path('servo/', views.ServoListCreateView.as_view(), name='servo-list-create'),
    path('servo/<int:pk>/', views.ServoDetailView.as_view(), name='servo-detail')
]

