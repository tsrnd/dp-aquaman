from django.urls import path, include
from django.urls import path
from yashoes.product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('filter', views.FilterProduct)

urlpatterns = [
    path('', views.ProductsAPIView.as_view()),
    path('<int:pk>', views.ProductDetail.as_view()),
    path('<int:product_id>/rating', views.RatingView.as_view()),
    path('<int:product_id>/comments', views.CommentView.as_view()),
    path('homepage', views.HomePageApiView.as_view()),
    path('',  include(router.urls))
]
