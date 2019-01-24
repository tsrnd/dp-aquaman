from django.urls import path
from yashoes_frontend.cart.views import cart_view, sync_cart

urlpatterns = [
    path('cart/', cart_view, name="cart"),
    path('sync/', sync_cart, name="sync"),
]

