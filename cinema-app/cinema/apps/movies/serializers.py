from rest_framework import serializers
from .models import Movie, Genre, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
