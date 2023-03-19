from random import choice
from textwrap import dedent


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
    # subject = 'Регистрация на сайте foodplan'
    # message = ''
    # send_mail(subject, message, settings.EMAIL_HOST_USER, user.email)


def profile(request, username):
    current_user = get_object_or_404(User, username=username)
    context = {
        'current_user': current_user,
        'user_plan': None,
    }
    plan = current_user.plan
    subscription = current_user.subscription

    if plan and subscription:
        menu = plan.menu
        allergy = plan.allergy
        allergy_description = allergy if allergy else 'У вас нет аллергии'
        persons_number = plan.persons_number
        dish_types = plan.dish_types
        plan_description = dedent(f'''
        Ваш план питания состоит из {len(dish_types)} приёмов пищи:
        {dish_types}. Ваша подписка закончится {subscription}.
        ''')

        user_plan = {
            'plan_description': plan_description,
            'allergy': allergy_description,
            'persons_number': persons_number,
            'meals_number': len(dish_types),
            'menu': menu,
        }
        context['user_plan'] = user_plan

    return render(request, 'users/profile.html', context)


def get_subscription_content(request, username, subscription_id):
    return render(request, 'meal_app/subscription_content.html')


def plan_user(request, username, user_plan_id):
    user_plan = Plan.objects.get(id=user_plan_id).get_recipies_user()
    context = []
    user_dish_type = [dish_type for dish_type in DISH_TYPE_CHOICE
                      if dish_type[0] in user_plan.dish_types]
    user_recipes = user_plan.user_recipes

    for dish_type in user_dish_type:
        user_dish_type = user_recipes.get(dish_type[0])
        if user_dish_type:
            recipe = choice(user_dish_type)
            ingredients = recipe.ingredients.split(', ')
            context.append(
                {
                 'dish_type': dish_type[1],
                 'title': recipe.title,
                 'description': recipe.description,
                 'image': recipe.image.url,
                 'calories': recipe.calories,
                 'ingredients': ingredients,
                }
            )
    return render(request, 'meal_app/subscription_content.html',
                  context={'context': context})
