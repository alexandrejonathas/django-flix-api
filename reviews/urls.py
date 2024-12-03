from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('api/reviews', views.ReviewListCreateView.as_view(), name='reviews_create_list'), # noqa
    path('api/reviews/<int:pk>', views.ReviewRetrieveUpdateDelete.as_view(), name='reviews_retrieve_update_delete'), # noqa
]
