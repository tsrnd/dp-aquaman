from django.urls import path

from yashoes_frontend.products.views import products, home, products_detail

urlpatterns = [
    path('home/', home, name="home"),
    path('products/', products, name="products"),
    path('products/detail/<int:product_id>', products_detail, name="product-detail")
]
