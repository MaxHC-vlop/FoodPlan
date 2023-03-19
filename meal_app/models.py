from django.utils import timezone
from django.db import models
from multiselectfield import MultiSelectField


INGREDIENT_TYPE_CHOICE = [
        ('FISH_AND_SEAFOOD', 'Рыба и морепродукты'),
        ('MEAT', 'Мясо'),
        ('GRAINS', 'Зерновые'),
        ('BEE_PRODUCTS', 'Продукты пчеловодства'),
        ('NUTS_AND_BEANS', 'Орехи и бобовые'),
        ('MILK_PRODUCTS', 'Молочные продукты')
    ]

DISH_TYPE_CHOICE = [
        ('BREAKFAST', 'Завтрак'),
        ('LUNCH', 'Обед'),
        ('DINNER', 'Ужин'),
        ('DESSERT', 'Десерт'),
    ]


class Menu(models.Model):
    MENU_CHOICES = [
        ('CLASSIC', 'Классическое'),
        ('LOW_CARB', 'Низкоуглеводное'),
        ('VEGITARIAN', 'Вегитарианское'),
        ('KETO', 'Кето')
    ]
    menu_type = models.CharField(
        'Тип меню',
        max_length=20,
        choices=MENU_CHOICES,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Тип меню'
        verbose_name_plural = 'Типы меню'

    def __str__(self):
        return self.menu_type


class Plan(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        related_name='plans',
        null=True,
        blank=True,
    )
    dish_types = MultiSelectField(
        'Типы блюд',
        choices=DISH_TYPE_CHOICE,
        max_choices=4,
        max_length=200,
        default=['BREAKFAST', 'LUNCH', 'DINNER', 'DESSERT'],
        db_index=True,
    )
    persons_number = models.PositiveSmallIntegerField(
        'Количество персон',
        default=1,
        db_index=True,
    )
    allergy = MultiSelectField(
        'Аллергия',
        choices=INGREDIENT_TYPE_CHOICE,
        max_choices=6,
        max_length=200,
        null=True,
        blank=True,
        db_index=True,
    )

    def get_recipies_user(self):
        user_allergies = self.allergy
        user_recipes_without_allergy = Recipe.objects.filter(
            dish_type__in=list(self.dish_types)
        )
        user_all_recipes = []
        for user_allergy in user_allergies:
            user_all_recipes += list(
                user_recipes_without_allergy
                .exclude(ingredient_types__contains=user_allergy)
            )
        user_recipes = {}
        for dish_type in DISH_TYPE_CHOICE:
            user_recipes[dish_type[0]] = []
        for recipe in user_recipes_without_allergy:
            if user_all_recipes.count(recipe) == len(user_allergies):
                user_recipes[recipe.dish_type].append(recipe)
        self.user_recipes = user_recipes
        return self

    class Meta:
        verbose_name = 'План питания'
        verbose_name_plural = 'Планы питания'

    def __str__(self):
        return f'Меню {self.menu} на {self.persons_number}'


class Recipe(models.Model):
    title = models.CharField('Название', max_length=100, db_index=True)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка')
    calories = models.DecimalField(
        'Калорийность (на 100 грамм)',
        max_digits=8,
        decimal_places=1,
        blank=True,
        db_index=True,
    )
    dish_type = models.CharField(
        'Тип блюда',
        choices=DISH_TYPE_CHOICE,
        max_length=20,
        db_index=True
    )
    ingredients = models.TextField('Ингредиенты')
    ingredient_types = MultiSelectField(
        'Типы ингредиентов',
        choices=INGREDIENT_TYPE_CHOICE,
        max_choices=6,
        max_length=200,
        null=True,
        blank=True,
        db_index=True,
    )
    menu = models.ManyToManyField(
        Menu,
        verbose_name='Меню',
        related_name='recipes',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class Subscription(models.Model):
    subscription_end_date = models.DateTimeField(
        'Дата окончания подписки',
        null=True,
        blank=True,
    )

    def available(self):
        if timezone.localtime(self.subscription_end_date) and \
                timezone.localtime(timezone.now()) <\
                self.subscription_end_date:
            return True

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.subscription_end_date.strftime("%d/%m/%Y, %H:%M:%S")
