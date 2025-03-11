from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.first_name