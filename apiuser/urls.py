from django.urls import path
from .views import UsuListView, UsuDetailView
from .views import UsuarioLoginView, UsuarioLogoutView
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('usuarios/', UsuListView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuDetailView.as_view(), name='usuario-detail'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('logout/', UsuarioLogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)