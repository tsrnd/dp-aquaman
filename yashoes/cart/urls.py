from django.urls import path
from yashoes.cart import views

urlpatterns = [
    path('variant/', views.UserVariantView.as_view())
]
