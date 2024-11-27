from django.urls import resolve, reverse

from django.test import TestCase

import json

class GenreApiTest(TestCase):

    def test_genre_api_list_endpoint(self):

        response = self.client.get(reverse('genres:list'))

        genres = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(genres['id']), 1)
