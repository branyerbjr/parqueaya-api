from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer, UsuarioLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

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
    def post(self, request):
        # Crear una instancia del serializador UsuarioLoginSerializer con los datos de la solicitud
        serializer = UsuarioLoginSerializer(data=request.data)
        
        # Verificar si los datos proporcionados son válidos según el serializador
        if serializer.is_valid():
            # Extraer el correo y la contraseña validados del serializador
            correo = serializer.validated_data['correo']
            password = serializer.validated_data['password']

            try:
                # Intentar obtener un usuario con el correo proporcionado
                user = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                # Manejar el caso en que no se encuentra el usuario
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

            # Autenticar al usuario utilizando el método `authenticate`
            if authenticate(request, correo=correo, password=password):
                # Si las credenciales son válidas, iniciar sesión y obtener o crear un token
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                # Devolver una respuesta con el token y los datos del usuario
                return Response({'token': token.key, 'user': UsuarioSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                # Manejar el caso en que las credenciales no son válidas
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Manejar el caso en que los datos no son válidos según el serializador
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        usuario = request.data.get('usuario')
        contraseña = request.data.get('contraseña')
        user = authenticate(request, usuario=usuario, contraseña=contraseña)

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
