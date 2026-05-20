# Generated for the Incubyte salary management assessment.

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("full_name", models.CharField(max_length=120)),
                ("job_title", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=80)),
                (
                    "salary",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("department", models.CharField(max_length=80)),
                (
                    "employment_type",
                    models.CharField(
                        choices=[
                            ("FULL_TIME", "Full time"),
                            ("PART_TIME", "Part time"),
                            ("CONTRACT", "Contract"),
                            ("INTERN", "Intern"),
                        ],
                        default="FULL_TIME",
                        max_length=20,
                    ),
                ),
                ("hire_date", models.DateField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["full_name"],
            },
        ),
    ]
