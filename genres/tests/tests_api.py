import json
from django.urls import reverse

from .tests_genre_base import GenreBaseTest


class GenreApiTest(GenreBaseTest):

    def test_api_resource_genres_method_not_allowed(self):

        response = self.client.patch(reverse('genres:genres_create_list'))

        self.assertEqual(response.status_code, 405)

    def test_api_resource_genres_list(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(reverse('genres:genres_create_list'))

        genres = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(genres), 2)
        self.assertEqual(int(genres[0]['id']), 1)
        self.assertEqual(genres[0]['name'], 'Ação')

    def test_api_resource_genres_create(self):

        genre = {'name': 'Terror'}
        
        response = self.client.post(
            reverse('genres:genres_create_list'), 
            data=json.dumps(genre),
            content_type='application/json'
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Terror')        

    def test_api_resource_genres_find_by_id(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1})
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Ação')

    def test_api_resource_genres_find_by_id_not_found(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, 404)

    def test_api_resource_genres_update(self):

        self.make_genre(name='Ação')

        response = self.client.put(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1}),
            data=json.dumps({'name': 'Comédia'}),
            content_type='application/json'
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Comédia')

    def test_api_resource_genres_update_not_found(self):

        self.make_genre(name='Ação')

        response = self.client.put(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 2}),
            data=json.dumps({'name': 'Comédia'})
        )

        self.assertEqual(response.status_code, 404)

    def test_api_resource_genres_delete(self):

        self.make_genre(name='Ação')

        response = self.client.delete(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1})
        )

        self.assertEqual(response.status_code, 204)

    def test_api_resource_genres_delete_not_found(self):

        self.make_genre(name='Ação')

        response = self.client.delete(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, 404)



