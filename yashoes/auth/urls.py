from .views import AuthView
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()

router.register(r'user', AuthView, basename='auth')

auth_urls = [
    path('user/login/', obtain_jwt_token, name="auth-login"),
    path('user/refresh-token/', refresh_jwt_token, name='auth-refresh-token'),
]
urlpatterns = router.urls + auth_urls
