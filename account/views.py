from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, UserRegistrSerializer
from .models import User


class RegistrUserView(CreateAPIView):
    """Регистрация пользователя"""

    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    """Выход из аккаунта"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status.HTTP_200_OK)


class LoginGenericAPIView(generics.GenericAPIView):
    """Аутентификация пользователя"""
    
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status.HTTP_200_OK)
