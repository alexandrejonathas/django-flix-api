import json
from datetime import date
from django.urls import reverse

from .tests_review_base import ReviewBaseTest


class ReviewApiTest(ReviewBaseTest):

    def test_api_resource_review_method_not_allowed(self):

        response = self.client.patch(reverse('reviews:reviews_create_list'))

        self.assertEqual(response.status_code, 405)

    def test_api_resource_movie_list(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.get(reverse('reviews:reviews_create_list'))

        reviews = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reviews), 2)

    def test_api_resource_review_create(self):

        self.make_genre(name='Ação')

        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        response = self.client.post(
            reverse('reviews:reviews_create_list'),
            data=json.dumps(
                { 
                    'movie': 1,
                    'stars': 5,
                    'comment': 'Ótimo filme de ação' 
                }
            ),
            content_type='application/json'
        )

        review = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(review['id']), 1)
        self.assertEqual(review['stars'], 5)
        self.assertEqual(review['comment'], 'Ótimo filme de ação')

    def test_api_resource_review_create_bad_request(self):

        self.make_genre(name='Ação')

        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        response = self.client.post(
            reverse('reviews:reviews_create_list'),
            data=json.dumps(
                { 
                    'movie': '',
                    'stars': 5,
                    'comment': 'Ótimo filme de ação' 
                }
            ),
            content_type='application/json'
        )

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['movie'], ["This field may not be null."])

    def test_api_resource_review_retrieve_not_found(self):

        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.get(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, 404)                  

    def test_api_resource_review_retrieve(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.get(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': 1})
        )

        review = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(review['id']), 1)
        self.assertEqual(review['stars'], 5) 

    def test_api_resource_review_update(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        review = self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.put(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': review.id}),
            data=json.dumps(
                { 
                    'movie': review.movie.id,
                    'stars': 3,
                    'comment': review.comment   
                }
            ),
            content_type='application/json'
        )        

        movie = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(movie['id']), review.movie.id)
        self.assertEqual(int(movie['stars']), 3)

    def test_api_resource_review_update_bad_request(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        review = self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.put(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': review.id}),
            data=json.dumps(
                { 
                    'movie': '',
                    'stars': 6,
                    'comment': review.comment   
                }
            ),
            content_type='application/json'
        )        

        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['movie'], ['This field may not be null.'])
        self.assertEqual(content['stars'], ['Ensure this value is less than or equal to 5.'])


    def test_api_resource_review_update_not_found(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        review = self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.put(
            reverse('movies:movies_retrieve_update_delete', kwargs={'pk': 3}),
            data=json.dumps(
                { 
                    'movie': review.movie.id,
                    'stars': 4,
                    'comment': 'Novo comentário'   
                }
            ),
            content_type='application/json'
        )        

        self.assertEqual(response.status_code, 404)


    def test_api_resource_review_delete(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        review = self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.delete(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': review.id}),
        )        

        self.assertEqual(response.status_code, 204)

    def test_api_resource_review_delete_not_found(self):
        
        denzel_washington = self.make_actor(name='Denzel Washington')
        marton_csokas = self.make_actor(name='Marton Csokas')

        movie = self.make_movie(title='The equalizer', actors_data=[denzel_washington, marton_csokas]) # noqa

        review = self.make_review(movie=movie)
        self.make_review(movie=movie, stars=4)

        response = self.client.delete(
            reverse('reviews:reviews_retrieve_update_delete', kwargs={'pk': 3}),
        )        

        self.assertEqual(response.status_code, 404)