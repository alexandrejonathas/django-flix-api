import json
from django.urls import reverse
from .tests_genre_base import GenreBaseTest

from genres.models import Genre

class GenreApiTest(GenreBaseTest):

    def setUp(self):
        self.userdata = {'username': 'user', 'password': 'password'}
        
        self.user = self.make_user(
            username=self.userdata.get('username'),
            password=self.userdata.get('password')
        )

    def test_api_resource_genres_method_not_allowed(self):

        self.make_user_permissions(user=self.user, model=Genre, perms=['view_genre', 'change_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.patch(
            reverse('genres:genres_create_list'),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 405)

    def test_api_resource_genres_list(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        self.make_user_permissions(user=self.user, model=Genre, perms=['view_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('genres:genres_create_list'),
            headers={'Authorization': f'Bearer {token}'}
        )

        genres = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(genres), 2)
        self.assertEqual(int(genres[0]['id']), 1)
        self.assertEqual(genres[0]['name'], 'Ação')

    def test_api_resource_genres_list_not_send_jwt_token(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        response = self.client.get(reverse('genres:genres_create_list'))

        self.assertEqual(response.status_code, 401)        

    def test_api_resource_genres_create(self):

        self.make_user_permissions(user=self.user, model=Genre, perms=['add_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        genre = {'name': 'Terror'}
        
        response = self.client.post(
            reverse('genres:genres_create_list'), 
            data=json.dumps(genre),
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Terror')        

    def test_api_resource_genres_find_by_id(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        self.make_user_permissions(user=self.user, model=Genre, perms=['view_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1}),
            headers={'Authorization': f'Bearer {token}'}
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Ação')

    def test_api_resource_genres_find_by_id_not_found(self):

        self.make_genre(name='Ação')
        self.make_genre(name='Drama')

        self.make_user_permissions(user=self.user, model=Genre, perms=['view_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 3}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)

    def test_api_resource_genres_update(self):

        self.make_genre(name='Ação')

        self.make_user_permissions(user=self.user, model=Genre, perms=['change_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.put(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1}),
            data=json.dumps({'name': 'Comédia'}),
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        genre = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(genre['id']), 1)
        self.assertEqual(genre['name'], 'Comédia')

    def test_api_resource_genres_update_not_found(self):

        self.make_genre(name='Ação')
        
        self.make_user_permissions(user=self.user, model=Genre, perms=['change_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.put(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 2}),
            data=json.dumps({'name': 'Comédia'}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)

    def test_api_resource_genres_delete(self):

        self.make_genre(name='Ação')

        self.make_user_permissions(user=self.user, model=Genre, perms=['delete_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.delete(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 1}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 204)

    def test_api_resource_genres_delete_not_found(self):

        self.make_genre(name='Ação')

        self.make_user_permissions(user=self.user, model=Genre, perms=['delete_genre'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.delete(
            reverse('genres:genres_retrieve_update_delete', kwargs={'pk': 2}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)



