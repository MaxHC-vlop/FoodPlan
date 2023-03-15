from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    plan = models.IntegerField(max_length=10)
    subscription = models.IntegerField(max_length=10)

    def __str__(self):
        return self.username