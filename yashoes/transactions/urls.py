from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TransactionViews

router = DefaultRouter()
router.register(r'user/transactions', TransactionViews, basename='transactions')
urlpatterns = router.urls + [
]