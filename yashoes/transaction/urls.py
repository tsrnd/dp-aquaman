from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TransactionViews, TransactionView

router = DefaultRouter()
router.register(r'transactions', TransactionViews, basename='transactions')
urlpatterns = router.urls + [
    path('transaction/', TransactionView.as_view())
]
