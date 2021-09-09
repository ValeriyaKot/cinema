from rest_framework import viewsets
from .models import Room
from . import serializers


class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
