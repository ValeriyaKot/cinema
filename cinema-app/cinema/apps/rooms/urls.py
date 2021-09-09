from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('rooms', views.RoomModelViewSet, basename='rooms')


urlpatterns = router.urls
