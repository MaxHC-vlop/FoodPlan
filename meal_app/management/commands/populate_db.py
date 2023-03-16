import json
from random import sample, randint

from django.core.management.base import BaseCommand
from meal_app.models import Menu, Recipe, Plan


class Command(BaseCommand):
    help = 'Populate DB with data'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='File path')

    def handle(self, *args, **kwargs):
        menu_types = ['CLASSIC', 'LOW_CARB', 'VEGITARIAN', 'KETO']
        dish_types = ['BREAKFAST', 'LUNCH', 'DINNER', 'DESSERT']
        allergy = ['FISH_AND_SEAFOOD', 'MEAT', 'GRAINS', 'BEE_PRODUCTS',
                   'NUTS_AND_BEANS', 'MILK_PRODUCTS']

        Menu.objects.all().delete()
        Plan.objects.all().delete()
        for menu_type in menu_types:
            menu = Menu.objects.create(menu_type=menu_type)
            Plan.objects.create(
                menu=menu,
                dish_types=sample(dish_types, 3),
                persons_number=randint(1, 6),
                allergy=sample(allergy, 2)
                )

        file = kwargs.get('file')
        with open(file, 'r') as file:
            raw_recipes = json.loads(file.read())
        all_menu = Menu.objects.all()

        Recipe.objects.all().delete()
        for raw_recipe in raw_recipes:
            obj = Recipe.objects.create(
                title=raw_recipe.get('title'),
                description=raw_recipe.get('description'),
                image=raw_recipe.get('image'),
                calories=raw_recipe.get('calories'),
                dish_type=raw_recipe.get('dish_type'),
                ingredients=raw_recipe.get('ingredients'),
                ingredient_types=raw_recipe.get('ingredient_types'),
            )

            suitable_menus = raw_recipe.get('menu').split(', ')
            for suitable_menu in suitable_menus:
                obj.menu.add(all_menu.get(menu_type=suitable_menu))
        print('Данные успешно добавлены')
