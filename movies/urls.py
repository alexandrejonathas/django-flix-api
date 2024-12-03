from django.urls import path

from movies import views

app_name = 'movies'

urlpatterns = [
    path('api/movies', views.MovieListCreateView.as_view(), name='movies_create_list'), # noqa
    path('api/movies/<int:pk>', views.MovieRetrieveUpdateDelete.as_view(), name='movies_retrieve_update_delete'), # noqa
]
