from rest_framework import viewsets
from .models import Director, Genre, Movie, MovieSession
from . import serializers


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related('genre', 'director')
    serializer_class = serializers.MovieSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class DirectorView(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = serializers.DirectorSerializer


class MovieSessionsModelViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = serializers.MovieSessionSerializer

    
