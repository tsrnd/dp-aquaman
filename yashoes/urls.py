from django.urls import path, include

urlpatterns = [
    path('', include('yashoes.auth.urls')),
    path('products/', include('yashoes.product.urls')),
    path('user/', include('yashoes.user.urls')),
    path('', include('yashoes.transaction.urls')),
    path('user/cart/', include('yashoes.cart.urls')),
]
