from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('/reviews', views.ReviewListCreateView.as_view(), name='reviews_create_list'), # noqa
    path('/reviews/<int:pk>', views.ReviewRetrieveUpdateDelete.as_view(), name='reviews_retrieve_update_delete'), # noqa
]
