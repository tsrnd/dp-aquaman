from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from yashoes.product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('filter', views.FilterProduct)

urlpatterns = [
    path('', views.ProductsAPIView.as_view()),
    path('<int:pk>', views.ProductDetail.as_view()),
    path('<int:product_id>/comments', views.CommentView.as_view()),
    path('',  include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)
