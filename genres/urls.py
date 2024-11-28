from django.urls import path

from genres import views

app_name = 'genres'

urlpatterns = [
    path('api/genres', views.genres_create_list_view, name='genres_resources'),
    path('api/genres/<int:genre_id>', views.genres_find_update_delete, name='genres_find_update_delete') # noqa
]