# MovieReviews/models.py

from django.db import models


class MovieManager(models.Manager):
    def high_rated(self):
        return self.filter(rating__gte=8)

    def recent_releases(self):
        return self.order_by('-release_date')


class Movie(models.Model):
    title = models.CharField(max_length=200)  # Campo de texto para el título de la película
    description = models.TextField()  # Campo de texto para la descripción
    rating = models.PositiveIntegerField()  # Campo numérico para la calificación (del 1 al 10)
    release_date = models.DateField()  # Campo de fecha para la fecha de lanzamiento

    objects = MovieManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
