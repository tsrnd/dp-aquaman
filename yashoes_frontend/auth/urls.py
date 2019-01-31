from django.urls import path
from yashoes_frontend.auth.views import login, register, active_account, logout

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('account/active/', active_account, name="active"),
    path('logout/', logout, name="logout"),
]

