from django.urls import path
from yashoes.rating import views

urlpatterns = [
    path('', views.RatingView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
