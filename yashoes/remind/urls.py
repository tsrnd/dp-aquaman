from rest_framework.routers import DefaultRouter

from .views import RemindViews

router = DefaultRouter()
router.register(r'remind', RemindViews, basename='remind')
urlpatterns = router.urls
