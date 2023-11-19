<<<<<<< HEAD
from django.urls import path
from .views import AdminListCreateView, AdminDetailView, AdminLoginView, AdminLogoutView

urlpatterns = [
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('logout/', AdminLogoutView.as_view(), name='admin-logout'),
]
=======
from django.urls import path
from .views import AdminListCreateView, AdminDetailView, AdminLoginView, AdminLogoutView

urlpatterns = [
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('logout/', AdminLogoutView.as_view(), name='admin-logout'),
]
>>>>>>> c96de7ee265198347df3f9c5d11e523b4645620e
