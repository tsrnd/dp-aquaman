from django.urls import path
from yashoes.brand import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.BrandViewSet, basename='brands')

urlpatterns = router.urls
