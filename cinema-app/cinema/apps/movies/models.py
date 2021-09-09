from django.db import models
from apps.rooms.models import Room


class Director(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250)
    publication_date = models.DateField()
    publication_country = models.CharField(max_length=250)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    language = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class MovieSession(models.Model):
    date = models.DateField()
    time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_sessions')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='movie_sessions', default=1)
