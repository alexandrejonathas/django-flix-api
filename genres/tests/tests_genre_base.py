# type: ignore
from core.tests import BaseTest
from genres.models import Genre

class GenreBaseTest(BaseTest):

    def make_genre(self, name='Padrão'):
        return Genre.objects.create(name=name)
              