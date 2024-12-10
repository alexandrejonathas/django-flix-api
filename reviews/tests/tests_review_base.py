from datetime import date
from core.tests import BaseTest

from genres.models import Genre
from actors.models import Actor
from movies.models import Movie
from reviews.models import Review


class ReviewBaseTest(BaseTest):

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
            movie.save()

        return movie
    
    def make_review(self, movie, stars=5, comment='Default comment'):

        return Review.objects.create(
            movie=movie,
            stars=stars,
            comment=comment
        )
