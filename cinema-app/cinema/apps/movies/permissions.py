from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.users.models import User


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(user=request.user)
        if user.is_manager is True:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj