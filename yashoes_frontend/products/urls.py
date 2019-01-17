from rest_framework.routers import DefaultRouter
from yashoes_frontend.products.views import MainTemplate
from django.urls import path


router = DefaultRouter()
router.register(r'', MainTemplate, basename='products')
urlpatterns = router.urls
