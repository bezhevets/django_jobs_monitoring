# Generated by Django 5.0.2 on 2024-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VacancyDjinni",
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
                ("web_id", models.IntegerField(unique=True)),
                ("title", models.CharField(max_length=255)),
                ("intro", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("company", models.CharField(max_length=255, null=True)),
                ("location", models.CharField(max_length=190, null=True)),
                (
                    "employment_type",
                    models.CharField(max_length=190, null=True),
                ),
                ("experience", models.CharField(max_length=100, null=True)),
                ("english", models.CharField(max_length=100, null=True)),
                ("reviews", models.IntegerField()),
                ("date", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Vacancy Djinni",
                "verbose_name_plural": "Vacancies Djinni",
            },
        ),
    ]
