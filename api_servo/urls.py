from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServoViewSet

router = DefaultRouter()
router.register(r'servo', ServoViewSet, basename='servo')

urlpatterns = [
    path('servo/', include(router.urls)),
]
