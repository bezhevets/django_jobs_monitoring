from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name = "Name job board"
        verbose_name_plural = "Name job boards"

    def __str__(self) -> str:
        return self.name
