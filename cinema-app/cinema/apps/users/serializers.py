from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import password_validation
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'auth_token', 'is_manager')

    def get_auth_token(self, obj):
        refresh = RefreshToken.for_user(user=obj)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_manager')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value
