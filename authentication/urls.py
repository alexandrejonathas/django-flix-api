from django.urls import path

from rest_framework_simplejwt import views

app_name = 'authentication'

urlpatterns = [
    path('/authentication/token', views.TokenObtainPairView.as_view(), name='auth_token'), # noqa
]
