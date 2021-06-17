from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
