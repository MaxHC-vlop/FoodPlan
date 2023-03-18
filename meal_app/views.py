from random import sample

from django.shortcuts import get_object_or_404, render

from .models import Recipe


def index(request):
    template = 'meal_app/index.html'
    all_recipe = list(Recipe.objects.all())
    recipes_quantity = 4
    some_recipes = sample(all_recipe, recipes_quantity)
    active_recipes = some_recipes.pop()
    context = {'active_recipes': active_recipes, 'some_recipes': some_recipes}
    return render(request, template, context=context)


def order(request):
    template = 'meal_app/order.html'
    return render(request, template)


def recipe(request, recipe_id):
    template = 'meal_app/recipe.html'
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.split(', ')
    context = {
         'dish_type': recipe.dish_type,
         'title': recipe.title,
         'description': recipe.description,
         'image': recipe.image.url,
         'calories': recipe.calories,
         'ingredients': ingredients,
    }
    return render(request, template, context={'recipe': context})
