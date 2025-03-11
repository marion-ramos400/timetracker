from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField

from .projects import projects

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id", default=None)
    start_dt = models.DateTimeField()
    created_dt = models.DateTimeField(auto_now=True)
    hours = models.IntegerField(default=0)
    description = models.CharField(max_length=128, default="")
    project = models.CharField(
        max_length=128,
        choices=((item, item) for item in projects)
    )

    def __str__(self):
        return self.id