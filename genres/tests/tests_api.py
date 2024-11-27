from django.urls import resolve, reverse

from .tests_genre_base import GenreBaseTest

import json

class GenreApiTest(GenreBaseTest):

    def test_api_resource_genres_list(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(reverse('genres:list'))

        genres = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(genres), 2)
        self.assertEqual(int(genres[0]['id']), 1)
        self.assertEqual(genres[0]['name'], 'Ação')
