from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Transaction_detailView, TransactionView

router = DefaultRouter()
router.register(r'transaction-detail', Transaction_detailView, basename='transaction-detail')
urlpatterns = router.urls + [
    path('transaction/', TransactionView.as_view())
]
