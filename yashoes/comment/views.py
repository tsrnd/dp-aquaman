from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from yashoes.model.product import Product
from yashoes.model.comment import Comment
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from datetime import date, timedelta, datetime


class CommentView(APIView):
    permission_classes = (AllowAny, )

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.user.id == comment.user.id:
            comment.soft_delete()
            return Response({"message": "success"})
        else:
            return Response({"error": "Can not delete other comment"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
