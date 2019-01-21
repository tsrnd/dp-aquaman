from django.urls import path
from yashoes_frontend.user.views import profile
urlpatterns = [
    path('user/profile/', profile, name="profile")
]

