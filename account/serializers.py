from rest_framework import serializers

from .models import User


class UserRegistrSerializer(serializers.ModelSerializer):
    """Регистрация"""

    password2 = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
 
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
            
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    """Аутентификация пользователя"""
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
