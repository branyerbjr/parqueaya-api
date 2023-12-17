from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer, UsuarioRegistrationSerializer, UsuarioLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class UsuarioRegistrationView(APIView):
    
    def post(self, request):
        serializer = UsuarioRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Corrección en la línea siguiente
            user_model = get_user_model()
            token, _ = Token.objects.get_or_create(user=user_model.objects.get(id=user.id))
            
            return Response({'token': token.key, 'user': UsuarioSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
class UsuarioLoginView(APIView):
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            correo = serializer.validated_data['correo']
            password = serializer.validated_data['password']

            try:
                user = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

            if password == user.password:
                # Corregir la línea para usar la instancia de User
                user_model = get_user_model()
                user_instance = user_model.objects.get(id=user.id)
                token, _ = Token.objects.get_or_create(user=user_instance)

                login(request, user)

                return Response({'token': token.key, 'user': UsuarioSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Contraseña inválida'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UsuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UsuarioLogoutView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Aquí puedes realizar cualquier lógica de logout necesaria
        # Por ejemplo, invalidar tokens, eliminar sesiones, etc.
        request.auth.delete()  # Eliminar el token de autenticación (si estás utilizando tokens)

        # Otros pasos de logout según tu implementación

        return Response({'detail': 'Logout exitoso'}, status=status.HTTP_200_OK)

class RecuperacionContrasena(APIView):
    # Implementa la lógica de recuperación de contraseña
    pass


class AdminListCreateView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout exitoso'})
