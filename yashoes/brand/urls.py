from django.urls import path
from yashoes.brand import views

urlpatterns = [path('', views.BrandAPIView.as_view())]
