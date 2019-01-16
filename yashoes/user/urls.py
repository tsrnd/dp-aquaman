from .views import UserView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

router.register(r'', UserView, basename='user')

urlpatterns = router.urls