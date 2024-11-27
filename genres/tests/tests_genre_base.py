from django.test import TestCase

from genres.models import Genre


class GenreBaseTest(TestCase):

    def make_genre(self, name='Padrão'):
        return Genre.objects.create(name=name)