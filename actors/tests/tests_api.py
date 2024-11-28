import json
from django.urls import reverse

from .tests_actor_base import ActorBaseTest


class ActorApiTest(ActorBaseTest):

    def test_api_resource_actor_method_not_allowed(self):

        response = self.client.patch(reverse('actors:actors_create_list'))

        self.assertEqual(response.status_code, 405)

    def test_api_resource_actor_list(self):

        self.make_actor(name='Silvester Stalone')
        self.make_actor(name='Sharon Stone')

        response = self.client.get(reverse('actors:actors_create_list'))

        actors = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(actors), 2)

    def test_api_resource_actor_create(self):

        response = self.client.post(
            reverse('actors:actors_create_list'),
            data=json.dumps({'name': 'Silvester Stalone'}),
            content_type='application/json'
        )

        actor = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(actor['id']), 1)
        self.assertEqual(actor['name'], 'Silvester Stalone')                   
