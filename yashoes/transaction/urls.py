from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TransactionView

router = DefaultRouter()
urlpatterns = router.urls + [
    path('transaction/', TransactionView.as_view())
]
