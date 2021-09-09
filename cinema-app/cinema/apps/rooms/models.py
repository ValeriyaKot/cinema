from django.db import models
from django.core.validators import MinValueValidator


class Room(models.Model):
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    isBooked = models.BooleanField(default=False)
