from django.urls import path
from yashoes_frontend.cart.views import cart_view

urlpatterns = [
    path('cart/', cart_view, name="cart"),
]

