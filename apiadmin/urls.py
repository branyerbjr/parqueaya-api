from django.urls import path
from .views import RegistroUsuario, InicioSesion, RecuperacionContrasena, AdminListCreateView, AdminDetailView, AdminLoginView, AdminLogoutView, UsuarioListView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('registro/', RegistroUsuario.as_view(), name='registro-usuario'),
    path('inicio-sesion/', InicioSesion.as_view(), name='inicio-sesion'),
    path('cerrar-sesion/', InicioSesion.as_view(action='logout'), name='cerrar-sesion'),
    path('recuperar-contrasena/', RecuperacionContrasena.as_view(), name='recuperar-contrasena'),
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('admin-logout/', AdminLogoutView.as_view(), name='admin-logout'),
]
