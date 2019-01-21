from .views import TransactionView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'transactions', TransactionView, basename='transactions')
urlpatterns = router.urls
