from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: 'Passwords does not match'})
        user.set_password(password)
        user.save()
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(max_length=255)
    password_2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2',]

