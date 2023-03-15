from django.contrib import admin
from .models import (Ingredient, Plan, Recipe, Subscription, Menu)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    raw_id_fields = ['ingredient', 'menu']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
