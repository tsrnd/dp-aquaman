from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from yashoes.model.product import Product
from yashoes.model.comment import Comment
from yashoes.comment.serializers import PostCommentSerializer, GetCommentsSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny


class GetCommentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, product_id):
        comment = Comment.objects.filter(product=product_id).filter(
            parent_comment=None)
        data = GetCommentsSerializer(comment, many=True).data
        return Response({"data": data})


class CreateCommentView(APIView):
    def post(self, request):
        product = request.data.get("product_id")
        content = request.data.get("content")
        parent_comment = request.data.get("parent_comment_id")
        data = {
            'product': product,
            'content': content,
            'parent_comment': parent_comment
        }
        serializer = PostCommentSerializer(
            data=data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
