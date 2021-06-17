from django.contrib import admin
from .models import Genre, Movie, Director, MovieSession


admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(MovieSession)
