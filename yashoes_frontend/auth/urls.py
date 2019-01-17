# from rest_framework.routers import DefaultRouter
# from yashoes_frontend.auth.views import DemoTemplate
# from django.urls import path


# router = DefaultRouter()
# router.register(r'', DemoTemplate, basename='what')
# urlpatterns = router.urls


from django.urls import path
from yashoes_frontend.auth.views import login, register

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]

