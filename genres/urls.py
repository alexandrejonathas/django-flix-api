from django.urls import path

from genres import views

urlpatterns = [
    path('api/genres', views.index),
]