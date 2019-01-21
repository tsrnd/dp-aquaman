from django.urls import path
from yashoes_frontend.products.views import products, home, productsdetail
urlpatterns = [
    path('home/', home, name="home"),
    path('products/', products, name="products"),
    path('products/detail/1', productsdetail, name="product-detail"),
]
