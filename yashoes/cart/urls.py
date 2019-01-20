from django.urls import path
from yashoes.cart import views

urlpatterns = [
    path('add_variant/', views.CreateCartVariant.as_view())
]
