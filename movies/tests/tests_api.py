import json
from datetime import date
from django.urls import reverse

from .tests_movie_base import MovieBaseTest


class MovieApiTest(MovieBaseTest):

    def test_api_resource_movie_method_not_allowed(self):

        response = self.client.patch(reverse('movies:movies_create_list'))

        self.assertEqual(response.status_code, 405)

    def test_api_resource_movie_list(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.get(reverse('movies:movies_create_list'))

        movies = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(movies), 2)

    def test_api_resource_movie_create(self):

        self.make_genre(name='Ação')
        self.make_actor(name='Denzel Washington')
        self.make_actor(name='Marton Csokas')

        response = self.client.post(
            reverse('movies:movies_create_list'),
            data=json.dumps(
                {
                    'title': 'The equalizer', 
                    'genre': 1,
                    'actors': [1, 2],
                    'release_date': '2014-09-25' 
                }
            ),
            content_type='application/json'
        )

        movie = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(movie['id']), 1)
        self.assertEqual(movie['title'], 'The equalizer')
        self.assertEqual(len(movie['actors']), 2)

    def test_api_resource_movie_create_bad_request(self):

        self.make_genre(name='Ação')
        self.make_actor(name='Denzel Washington')
        self.make_actor(name='Marton Csokas')

        response = self.client.post(
            reverse('movies:movies_create_list'),
            data=json.dumps(
                {
                    'title': '', 
                    'genre': 1,
                    'actors': [1, 2],
                    'release_date': '2014-09-25' 
                }
            ),
            content_type='application/json'
        )

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['title'], ['This field may not be blank.'])

    def test_api_resource_movie_retrieve_not_found(self):

        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.get(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 3}),
        )

        self.assertEqual(response.status_code, 404)                  

    def test_api_resource_movie_retrieve(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(
            title='The equalizer', 
            actors_data=[denzel_washington, marton_csokas],
            release_date=date(2014, 9, 25)
        ) # noqa
        self.make_movie(
            title='The equalizer 2', 
            actors_data=[denzel_washington, pedro_pascal],
            release_date=date(2018, 7, 19)
        ) # noqa

        response = self.client.get(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 1}),
        )

        movie = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(movie['id']), 1)
        self.assertEqual(movie['title'], 'The equalizer') 

    def test_api_resource_movie_update(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.put(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 1}),
            data=json.dumps(
                {
                    'title': 'The equalizer 3', 
                    'genre': 1,
                    'actors': [1, 2],
                    'release_date': '2014-09-25'   
                }
            ),
            content_type='application/json'
        )        

        movie = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(movie['id']), 1)
        self.assertEqual(movie['title'], 'The equalizer 3')

    def test_api_resource_movie_update_bad_request(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.put(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 1}),
            data=json.dumps(
                {
                    'title': '', 
                    'genre': 1,
                    'actors': [1, 2],
                    'release_date': '2014-09-25'   
                }
            ),
            content_type='application/json'
        )        

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['title'], ['This field may not be blank.'])


    def test_api_resource_movie_update_not_found(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.put(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 3}),
            data=json.dumps(
                {
                    'title': 'The equalizer 3', 
                    'genre': 1,
                    'actors': [1, 2]   
                }
            ),
            content_type='application/json'
        )        

        self.assertEqual(response.status_code, 404)


    def test_api_resource_movie_delete(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.delete(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 2}),
        )        

        self.assertEqual(response.status_code, 204)

    def test_api_resource_movie_delete_not_found(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')
        pedro_pascal = self.make_actor(name='Pedro Pascal')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa
        self.make_movie(title='The equalizer 2', actors_data=[denzel_washington, pedro_pascal]) # noqa

        response = self.client.delete(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 3}),
        )        

        self.assertEqual(response.status_code, 404)