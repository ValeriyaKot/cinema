from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    # path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('token/', views.token),
    path('register/', views.register),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
]
