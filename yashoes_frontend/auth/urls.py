from rest_framework.routers import DefaultRouter
from yashoes_frontend.auth.views import DemoTemplate
from django.urls import path


router = DefaultRouter()
router.register(r'', DemoTemplate, basename='what')
urlpatterns = router.urls
