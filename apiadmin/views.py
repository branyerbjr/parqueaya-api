from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer, UsuarioLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
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
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, correo=serializer.validated_data['correo'], contrasena=serializer.validated_data['contrasena'])
            if user and check_password(serializer.validated_data['contrasena'], user.password):
                print('Usuario autenticado')
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({
                    'message': 'Inicio de sesión exitoso',
                    'refresh': str(refresh),
                    'access': access_token,
                })
            else:
                print('Credenciales inválidas')
                return Response({'error': 'Credenciales inválidas'}, status=401)
        return Response(serializer.errors, status=400)


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
