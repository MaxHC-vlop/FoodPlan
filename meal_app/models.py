from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from multiselectfield import MultiSelectField


ALLERGY_CHOICES = [
        ('NO_ALLERGY', 'Нет аллергии'),
        ('FISH_AND_SEAFOOD', 'Рыба и морепродукты'),
        ('MEAT', 'Мясо'),
        ('GRAINS', 'Зерновые'),
        ('BEE_PRODUCTS', 'Продукты пчеловодства'),
        ('NUTS_AND_BEANS', 'Орехи и бобовые'),
        ('MILK_PRODUCTS', 'Молочные продукты')
    ]


class Ingredient(models.Model):
    CHOOSE_MEASURE = [
        ('GRAM', 'гр'),
        ('MILLILITER', 'мл'),
        ('THING', 'шт'),
        ('TEASPOON', 'ч.л.'),
        ('TABLESPOON', 'ст.л.'),
    ]
    title = models.CharField('Название', max_length=100, db_index=True)
    measure = models.CharField(
        'Мера измерения',
        max_length=20,
        choices=CHOOSE_MEASURE,
        blank=True,
    )
    quantity = models.CharField('Количество', max_length=30)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.title


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
    breakfast = models.BooleanField('Завтрак', default=True, db_index=True,)
    lunch = models.BooleanField('Обед', default=True, db_index=True,)
    dinner = models.BooleanField('Ужин', default=True, db_index=True,)
    dessert = models.BooleanField('Десерт', default=True, db_index=True,)
    persons_number = models.PositiveSmallIntegerField(
        'Количество персон',
        default=1,
        db_index=True,
    )
    allergy = MultiSelectField(
        'Алергия',
        choices=ALLERGY_CHOICES,
        max_choices=6,
        max_length=200,
        default='NO_ALLERGY',
        db_index=True,
    )

    class Meta:
        verbose_name = 'План питания'
        verbose_name_plural = 'Планы питания'

    def __str__(self):
        return f'Меню {self.menu} на {self.persons_number} персон'


class Recipe(models.Model):
    CHOOSE_TYPE_DISH = [
        ('breakfast', 'завтрак'),
        ('lunch', 'обед'),
        ('dinner', 'ужин'),
        ('dessert', 'десерт'),
    ]
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
        choices=CHOOSE_TYPE_DISH,
        max_length=20,
        db_index=True
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='recipes'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.SET_NULL,
        related_name='recipes',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class SubscriptionQuerySet(models.QuerySet):
    def available(self):  # Это возможно не будет работать, нужно тестить
        if self.subscription_end_date\
                and datetime.now() < self.subscription_end_date:
            return True

    def set_subscription_end_date(self, months_quantity):
        self.subscription_end_date = datetime.now() +\
            relativedelta(months=months_quantity)


class Subscription(models.Model):
    subscription_end_date = models.DateTimeField(
        'Дата окончания подписки',
        null=True,
        blank=True,
    )
    objects = SubscriptionQuerySet.as_manager()

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Окончание подписки {self.subscription_end_date}'
