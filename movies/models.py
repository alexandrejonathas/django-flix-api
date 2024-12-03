from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    resume = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies'
    )
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title
