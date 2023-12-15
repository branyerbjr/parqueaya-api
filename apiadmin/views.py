from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Admin, Usuario
from .serializers import AdminSerializer, UsuarioSerializer, UsuarioLoginSerializer, UsuarioRegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class UsuarioRegistrationView(APIView):
    def post(self, request):
        serializer = UsuarioRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UsuarioSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioRegistrationView(APIView):
    def post(self, request):
        serializer = UsuarioRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UsuListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')  # Recupera el ID del usuario de los parámetros de la URL
        if user_id:
            # Si se proporciona un ID, recupera un usuario específico
            user = get_object_or_404(Usuario, id=user_id)
            serializer = UsuarioSerializer(user)
            return Response(serializer.data)
        else:
            # Si no se proporciona un ID, realiza la lista completa
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
