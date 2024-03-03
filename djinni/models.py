from django.db import models
from django.utils.timezone import now


class VacancyDjinni(models.Model):
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=190, null=True)
    employment_type = models.CharField(max_length=190, null=True)
    experience = models.CharField(max_length=100, null=True)
    english = models.CharField(max_length=100, null=True)
    reviews = models.IntegerField()
    date = models.DateTimeField()
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Vacancy Djinni"
        verbose_name_plural = "Vacancies Djinni"

    def __str__(self) -> str:
        return f"{self.company} is looking for a {self.title} with experience {self.experience}"
