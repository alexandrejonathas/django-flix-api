from django.urls import path

from genres import views

app_name = 'genres'

urlpatterns = [
    path('api/genres', views.GenreListCreateView.as_view(), name='genres_create_list'), # noqa
    path('api/genres/<int:pk>', views.GenreRetrieveUpdateDelete.as_view(), name='genres_retrieve_update_delete') # noqa
]