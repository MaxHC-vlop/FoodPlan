# Generated by Django 4.1.7 on 2023-03-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_plan_alter_user_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "This email address is already in use."},
                max_length=254,
                unique=True,
                verbose_name="Email address",
            ),
        ),
    ]
