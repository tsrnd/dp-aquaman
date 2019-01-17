from django.urls import path, include

urlpatterns = [
    path('', include('yashoes.auth.urls')),
    path('products/', include('yashoes.product.urls')),
    path('users/', include('yashoes.user.urls')),
    path('comments/', include('yashoes.comment.urls')),
    path('', include('yashoes.transaction.urls')),
    path('cart/', include('yashoes.cart.urls')),
]
