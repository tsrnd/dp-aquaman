from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from yashoes.product import views

urlpatterns = [
    path('', views.ProductsAPIView.as_view()),
    path('<int:pk>', views.ProductDetail.as_view()),
    path('<int:product_id>/comments', views.CommentView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
