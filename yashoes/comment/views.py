from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from yashoes.model.product import Product
from yashoes.model.comment import Comment
from yashoes.comment.serializers import GetCommentsSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny


class GetCommentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, product_id):
        comment = Comment.objects.filter(product=product_id).filter(
            parent_comment=None)
        data = GetCommentsSerializer(comment, many=True).data
        return Response({"data": data})