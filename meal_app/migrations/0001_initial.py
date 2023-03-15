# Generated by Django 4.1.7 on 2023-03-15 11:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес в граммах')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(choices=[('CLASSIC', 'Классическое'), ('LOW_CARB', 'Низкоуглеводное'), ('VEGITARIAN', 'Вегитарианское'), ('KETO', 'Кето')], db_index=True, max_length=20, verbose_name='Вид меню')),
                ('breakfast', models.BooleanField(db_index=True, default=True, verbose_name='Завтрак')),
                ('lunch', models.BooleanField(db_index=True, default=True, verbose_name='Обед')),
                ('dinner', models.BooleanField(db_index=True, default=True, verbose_name='Ужин')),
                ('dessert', models.BooleanField(db_index=True, default=True, verbose_name='Десерт')),
                ('persons_number', models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Количество персон')),
                ('allergy', multiselectfield.db.fields.MultiSelectField(choices=[('NO_ALLERGY', 'Нет аллергии'), ('FISH_AND_SEAFOOD', 'Рыба и морепродукты'), ('MEAT', 'Мясо'), ('GRAINS', 'Зерновые'), ('BEE_PRODUCTS', 'Продукты пчеловодства'), ('NUTS_AND_BEANS', 'Орехи и бобовые'), ('MILK_PRODUCTS', 'Молочные продукты')], db_index=True, default='NO_ALLERGY', max_length=20, verbose_name='Алергия')),
            ],
            options={
                'verbose_name': 'План питания',
                'verbose_name_plural': 'Планы питания',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания подписки')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('calories', models.PositiveIntegerField(blank=True, db_index=True, verbose_name='Общая калорийность на 1 персону')),
                ('dish_type', models.IntegerField(choices=[(1, 'breakfast'), (2, 'lunch'), (3, 'dinner'), (4, 'dessert')], db_index=True, verbose_name='Тип блюда')),
                ('ingredient', models.ManyToManyField(related_name='recipes', to='meal_app.ingredient', verbose_name='Ингредиенты')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='meal_app.plan', verbose_name='План')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]