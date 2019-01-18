from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from yashoes.comment import views

urlpatterns = [
    path('<int:comment_id>', views.CommentView.as_view()),
]
