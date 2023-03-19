from random import sample
from dateutil.relativedelta import relativedelta

from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from users.models import User
from .models import (Recipe, Plan, Menu, Subscription,
                     DISH_TYPE_CHOICE, INGREDIENT_TYPE_CHOICE)


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
    if request.method == 'POST' and request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        # if user.subscription and user.subscription.available():
        #     return redirect(reverse('users:profile',
        #                             kwargs={'username': user.username})
        #                     )
        menu = request.POST.get('foodtype')
        if not menu:
            return render(request, template)
        months_quantity = int(request.POST.get('TIME'))
        dish_types = []
        for dish_type in DISH_TYPE_CHOICE:
            if int(request.POST.get(dish_type[0])):
                dish_types.append(dish_type[0])
        persons_number = request.POST.get('person')
        allergy = []

        for number in range(len(INGREDIENT_TYPE_CHOICE)):
            one_allergy = request.POST.get(f'allergy{number}')
            if one_allergy:
                allergy.append(one_allergy)
        user_plan, _ = Plan.objects.get_or_create(
            menu=Menu.objects.get(menu_type=menu),
            dish_types=dish_types,
            persons_number=persons_number,
            allergy=allergy,
        )
        if not user.subscription and not user.subscription.available():
            subscription = Subscription.objects.create(
                subscription_end_date=timezone.localtime(timezone.now()) +
                relativedelta(months=months_quantity)
            )
            user.subscription = subscription
        user.plan = user_plan
        user.save()
        template = 'users.profile.html'

        return redirect(reverse('users:profile',
                                kwargs={'username': user.username})
                        )

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
