from django.urls import path

from actors import views

app_name = 'actors'

urlpatterns = [
    path('api/actors', views.ActorListCreateView.as_view(), name='actors_create_list'), # noqa
    path('api/actors/<int:pk>', views.ActorRetrieveUpdateDelete.as_view(), name='actors_retrieve_update_delete') # noqa
]
