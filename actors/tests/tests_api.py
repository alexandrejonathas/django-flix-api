import json
from django.urls import reverse

from .tests_actor_base import ActorBaseTest
from actors.models import Actor


class ActorApiTest(ActorBaseTest):

    def setUp(self):
        self.userdata = {'username': 'user', 'password': 'password'}
        
        self.user = self.make_user(
            username=self.userdata.get('username'),
            password=self.userdata.get('password')
        )

    def test_api_resource_actor_method_not_allowed(self):

        self.make_user_permissions(user=self.user, model=Actor, perms=['view_actor', 'change_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.patch(
            reverse('actors:actors_create_list'),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 405)

    def test_api_resource_actor_list(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['view_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('actors:actors_create_list'),
            headers={'Authorization': f'Bearer {token}'}
        )

        actors = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(actors), 2)

    def test_api_resource_actor_create(self):

        self.make_user_permissions(user=self.user, model=Actor, perms=['add_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.post(
            reverse('actors:actors_create_list'),
            data=json.dumps({'name': 'Silvester Stalone'}),
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        actor = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(actor['id']), 1)
        self.assertEqual(actor['name'], 'Silvester Stalone')

    def test_api_resource_actor_retrieve_not_found(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['view_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 3}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)                  

    def test_api_resource_actor_retrieve(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['view_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.get(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 1}),
            headers={'Authorization': f'Bearer {token}'}
        )

        actor = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(actor['id']), 1)
        self.assertEqual(actor['name'], 'Silvester Stalone')  

    def test_api_resource_actor_update(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['change_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.put(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 1}),
            data=json.dumps({'name': 'Jack Chan'}),
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        actor = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(actor['id']), 1)
        self.assertEqual(actor['name'], 'Jack Chan') 

    def test_api_resource_actor_update_not_found(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['change_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.put(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 3}),
            data=json.dumps({'name': 'Jack Chan'}),
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)

    def test_api_resource_actor_delete(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['delete_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.delete(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 1}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 204)

    def test_api_resource_actor_delete_not_found(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        self.make_user_permissions(user=self.user, model=Actor, perms=['delete_actor'])  # noqa
        token = self.get_jwt_token(userdata=self.userdata)

        response = self.client.delete(
            reverse('actors:actors_retrieve_update_delete', kwargs={'pk': 3}),
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 404)  