from .views import Transaction_detailView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'transaction-detail', Transaction_detailView, basename='transaction-detail')
urlpatterns = router.urls