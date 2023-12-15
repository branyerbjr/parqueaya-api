from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UsuListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuDetailView.as_view(), name='usuario-detail'),
    path('registro/', views.UsuarioRegistrationView.as_view(), name='registro-usuario'),
    path('inicio-sesion/', views.UsuarioLoginView.as_view(), name='inicio-sesion'),
    path('recuperar-contrasena/', views.RecuperacionContrasena.as_view(), name='recuperar-contrasena'),
    path('admins/', views.AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:pk>/', views.AdminDetailView.as_view(), name='admin-detail'),
    path('admin-login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('admin-logout/', views.AdminLogoutView.as_view(), name='admin-logout'),
]
