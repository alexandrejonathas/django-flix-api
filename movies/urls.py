from django.urls import path

from movies import views

app_name = 'movies'

urlpatterns = [
    path('/movies', views.MovieListCreateView.as_view(), name='movies_create_list'), # noqa
    path('/movies/<int:pk>', views.MovieRetrieveUpdateDelete.as_view(), name='movies_retrieve_update_delete'), # noqa
]
