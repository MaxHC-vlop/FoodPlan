from random import choice
from pprint import pprint
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CreationForm
from meal_app.models import Plan, DISH_TYPE_CHOICE
from .models import User

class SignUp(CreateView):
    form_class = CreationForm

    success_url = reverse_lazy('meal_app:index')
    template_name = 'users/signup.html'


def profile(request, username):
    current_user = get_object_or_404(User, username=username)
    print(current_user.first_name)
    context = {
        'current_user': current_user
    }

    return render(request, 'users/profile.html', context)


def plan_user(request, user_plan_id):
    user_plan = Plan.objects.get(id=user_plan_id).get_recipies_user()
    context = []
    user_dish_type = [dish_type for dish_type in DISH_TYPE_CHOICE
                      if dish_type[0] in user_plan.dish_types]
    print(user_dish_type)
    user_recipes = user_plan.user_recipes
    for dish_type in user_dish_type:
        recipe = choice(user_recipes.get(dish_type[0]))
        if recipe:
            context.append(
                {
                 'dish_type': dish_type[1],
                 'title': recipe.title,
                 'description': recipe.description,
                 'image': recipe.image,
                 'calories': recipe.calories,
                 'ingredients': recipe.ingredients,
                }
            )
        else:
            context.append(None)
    return render(request, 'meal_app/card3.html',
                  context={'context': context})
