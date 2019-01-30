from rest_framework.routers import DefaultRouter

from yashoes.category.views import CategoryView

router = DefaultRouter()
router.register('categories', CategoryView, basename='categories')

urlpatterns = router.urls
