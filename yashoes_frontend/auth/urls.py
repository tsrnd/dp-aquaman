from django.urls import path
from yashoes_frontend.auth.views import login, register

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]

