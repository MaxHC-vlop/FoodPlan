from django.contrib.auth.models import AbstractUser
from django.db import models
from meal_app.models import Plan, Subscription

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    plan = models.ForeignKey(
        Plan,
        verbose_name='План',
        on_delete=models.SET_NULL,
        related_name='users',
        null=True,
        blank=True
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.SET_NULL,
        related_name='users',
        null=True,
        blank=True
    )
    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={
            "unique": _("This email address is already in use.")
        },
    )

    plan = models.IntegerField(default=1)
    subscription = models.IntegerField(default=1)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username