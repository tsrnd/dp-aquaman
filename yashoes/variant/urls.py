from django.urls import path
from yashoes.variant import views

urlpatterns = [path('color/', views.ColorVariantAPIView.as_view())]
