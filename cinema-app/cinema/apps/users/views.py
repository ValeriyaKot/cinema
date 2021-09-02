from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, views, status, mixins
from .models import User
import requests
from . import serializers
from .utils import get_and_authenticate_user, create_user_account
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

CLIENT_ID = 'cinema'
CLIENT_SECRET = 'cinema-secret'

class LoginAPIView(views.APIView):

    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


# class RegisterAPIView(views.APIView):
#
#     def post(self, request):
#         serializer = serializers.UserSerializer(data=request.data)
#         if serializer.is_valid:
#             # user = create_user_account(**serializer.validated_data)
#             serializer.save()
#             r = requests.post('http://0.0.0.0:8000/o/token/',
#                               data={
#                                   'grant_type': 'password',
#                                   'username': request.data['username'],
#                                   'password': request.data['password'],
#                                   'client_id': CLIENT_ID,
#                                   'client_secret': CLIENT_SECRET,
#                               },
#                               )
#             # data = serializers.AuthUserSerializer(user).data
#             return Response(r.json())
#         return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer
    serializer = serializers.UserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differentley
        r = requests.post('http://0.0.0.0:8000/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    'http://0.0.0.0:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://0.0.0.0:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://0.0.0.0:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)

