from django.urls import path
from yashoes.cart import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.Cart, basename='cart')

urlpatterns = router.urls + [
    path('variant/', views.UserVariantView.as_view())
]
