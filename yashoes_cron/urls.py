from django.urls import path, include
from .hi import test

urlpatterns = [
    path('', test, name="test"),
]
