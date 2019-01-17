from django.urls import path, include

urlpatterns = [
    path('', include('yashoes_frontend.auth.urls')),
]
