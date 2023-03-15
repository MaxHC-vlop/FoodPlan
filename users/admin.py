from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User as CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser)
