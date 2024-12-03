from datetime import date
from django.test import TestCase

from genres.models import Genre
from actors.models import Actor
from movies.models import Movie


class MovieBaseTest(TestCase):

    def make_genre(self, name='Padrão'):
        return Genre.objects.create(name=name)

    def make_actor(self, name='Padrão', nationality=('USA', 'Estados Unidos')):
        return Actor.objects.create(name=name, nationality=nationality)
    
    def make_movie(
        self, 
        title = 'Default title',
        resume = 'Default resume',
        release_date =  date.today(),
        genre_data = None,
        actors_data = None 
    ):
        if not genre_data:
            genre_data = {}

        if not actors_data:
            actors_data = {}

        movie = Movie(
            title=title,
            release_date=release_date,
            resume=resume,
            genre=self.make_genre(**genre_data),            
        )

        movie.save()

        if actors_data:
            for actor in actors_data:
                movie.actors.add(actor)

        return movie.save()