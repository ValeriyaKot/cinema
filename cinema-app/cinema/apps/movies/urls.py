from rest_framework import routers
from .models import Genre, Movie, Director
from . import views

router = routers.SimpleRouter()
router.register('movies', views.MovieView, basename='movies')
router.register('directors', views.DirectorView, basename='directors')
router.register('genres', views.GenreView, basename='genres')


urlpatterns = router.urls
