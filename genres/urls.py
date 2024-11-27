from django.urls import path

from genres import views

app_name = 'genres'

urlpatterns = [
    path('api/genres', views.index, name='list'),
]