from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistroUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Encriptar la contraseña antes de almacenarla en la base de datos
        password = self.request.data.get('password')
        hashed_password = make_password(password)
        serializer.save(correo=self.request.data.get('correo'), password=hashed_password)

class InicioSesion(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        password = request.data.get('password')

        print(f'Correo: {correo}, Contraseña: {password}')

        # Utiliza el modelo Usuario para autenticar
        user = Usuario.objects.filter(correo=correo).first()

        if user and check_password(password, user.password):
            print('Usuario autenticado')
            login(request, user)

            # Utilizar el token proporcionado por Django Rest Framework
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'Inicio de sesión exitoso',
                'token': token.key,
            })
        else:
            print('Credenciales inválidas')
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        

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
