from django.urls import resolve, reverse

from .tests_genre_base import GenreBaseTest

import json

class GenreApiTest(GenreBaseTest):

    def test_api_resource_genres_method_not_allowed(self):

        response = self.client.patch(reverse('genres:genres_resources'))

        self.assertEqual(response.status_code, 405)

    def test_api_resource_genres_list(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(reverse('genres:genres_resources'))

        genres = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(genres), 2)
        self.assertEqual(int(genres[0]['id']), 1)
        self.assertEqual(genres[0]['name'], 'Ação')

    def test_api_resource_genres_create(self):

        genre = {'name': 'Terror'}
        
        response = self.client.post(
            reverse('genres:genres_resources'), 
            data=json.dumps(genre),
            content_type='application/json'
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Terror')        
