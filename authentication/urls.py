from django.urls import path

from rest_framework_simplejwt import views

app_name = 'authentication'

urlpatterns = [
    path('/authentication/token', views.TokenObtainPairView.as_view(), name='token'), # noqa
    path('/authentication/refresh-token', views.TokenRefreshView.as_view(), name='refresh_token'), # noqa
    path('/authentication/verify-token', views.TokenVerifyView.as_view(), name='verify_token'), # noqa
]
