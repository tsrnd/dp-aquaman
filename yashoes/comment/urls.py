from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from yashoes.comment import views

urlpatterns = [
    path(
        '<int:product_id>/',
        views.GetCommentView.as_view(),
        name="get_comment")
]
