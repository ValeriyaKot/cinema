from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, views, status, mixins
from .models import User
from . import serializers
from .utils import get_and_authenticate_user, create_user_account


class LoginAPIView(views.APIView):

    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


class RegisterAPIView(views.APIView):

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        user.save()
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)
