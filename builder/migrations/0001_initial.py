# Generated by Django 5.0.7 on 2024-09-16 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalDetails",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("job_title", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("job_description", models.TextField()),
                (
                    "personal_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="builder.personaldetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                ("institution", models.CharField(max_length=200)),
                ("degree", models.CharField(max_length=100)),
                ("start_year", models.IntegerField()),
                ("end_year", models.IntegerField()),
                (
                    "personal_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="builder.personaldetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("skill_name", models.CharField(max_length=50)),
                (
                    "personal_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="builder.personaldetails",
                    ),
                ),
            ],
        ),
    ]
