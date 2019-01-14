from .views import AuthView, DetailView
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()

router.register(r'', AuthView, basename='user')
router.register(r'user', DetailView, basename='user')

auth_urls = [
    path('login/', obtain_jwt_token, name="auth-login"),
    path('refresh-token/', refresh_jwt_token, name='auth-refresh-token'),
]
urlpatterns = router.urls + auth_urls
