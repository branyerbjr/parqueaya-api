# servicios/urls.py

from django.urls import path
from .views import MetodoPagoListCreateView, MetodoPagoDetailView, TransaccionListCreateView, TransaccionDetailView, DevolucionListCreateView, DevolucionDetailView, RegistroPagosListCreateView, RegistroPagosDetailView, TarifaListCreateView, TarifaDetailView

urlpatterns = [
    path('metodo-pago/', MetodoPagoListCreateView.as_view(), name='metodo-pago-list-create'),
    path('metodo-pago/<int:pk>/', MetodoPagoDetailView.as_view(), name='metodo-pago-detail'),
    path('transaccion/', TransaccionListCreateView.as_view(), name='transaccion-list-create'),
    path('transaccion/<int:pk>/', TransaccionDetailView.as_view(), name='transaccion-detail'),
    path('devolucion/', DevolucionListCreateView.as_view(), name='devolucion-list-create'),
    path('devolucion/<int:pk>/', DevolucionDetailView.as_view(), name='devolucion-detail'),
    path('registro-pagos/', RegistroPagosListCreateView.as_view(), name='registro-pagos-list-create'),
    path('registro-pagos/<int:pk>/', RegistroPagosDetailView.as_view(), name='registro-pagos-detail'),
    path('tarifa/', TarifaListCreateView.as_view(), name='tarifa-list-create'),
    path('tarifa/<int:pk>/', TarifaDetailView.as_view(), name='tarifa-detail'),
]
