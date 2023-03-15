from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    plan = models.IntegerField(default=1)
    subscription = models.IntegerField(default=1)

    def __str__(self):
        return self.username