from .views import Transaction_listlView
# from .views import Transaction_detailView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'transactions', Transaction_listlView, basename='transactions')

urlpatterns = router.urls