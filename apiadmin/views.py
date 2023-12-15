from django.shortcuts import render
import requests
from rest_framework import generics, permissions
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistroUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(correo=self.request.data.get('correo'))

class InicioSesion(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        password = request.data.get('password')

        print(f'Correo: {correo}, Contraseña: {password}')

        user = authenticate(request, correo=correo, password=password)

        if user and check_password(password, user.password):
            print('Usuario autenticado')
            login(request, user)

            # Generar tokens utilizando SimpleJWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'message': 'Inicio de sesión exitoso',
                'refresh': str(refresh),  # Esto podría cambiarse a 'str(refresh.access_token)' si es necesario
                'access': access_token,
            })
        else:
            print('Credenciales inválidas')
            return Response({'error': 'Credenciales inválidas'}, status=401)
        

class RecuperacionContrasena(APIView):
    # Implementa la lógica de recuperación de contraseña
    pass




class AdminListCreateView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        contraseña = request.data.get('contraseña')
        user = authenticate(request, correo=correo, contraseña=contraseña)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=401)


class AdminLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout exitoso'})
