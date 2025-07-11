# Generated by Django 5.1.5 on 2025-06-09 20:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "idade",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(18)]
                    ),
                ),
                ("cpf", models.CharField(max_length=11)),
            ],
        ),
    ]
