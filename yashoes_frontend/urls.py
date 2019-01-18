from django.urls import path, include

urlpatterns = [
    path('', include('yashoes_frontend.auth.urls')),
    path('', include('yashoes_frontend.products.urls')),
    path('', include('yashoes_frontend.cart.urls')),
]
