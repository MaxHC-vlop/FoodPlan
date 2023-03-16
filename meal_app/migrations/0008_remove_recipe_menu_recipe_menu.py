# Generated by Django 4.1.7 on 2023-03-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0007_alter_recipe_ingredient_types_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='menu',
        ),
        migrations.AddField(
            model_name='recipe',
            name='menu',
            field=models.ManyToManyField(db_index=True, related_name='recipes', to='meal_app.menu', verbose_name='Меню'),
        ),
    ]