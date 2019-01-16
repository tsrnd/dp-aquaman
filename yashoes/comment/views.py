from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from yashoes.model.product import Product
from yashoes.model.comment import Comment
from yashoes.comment.serializers import PostCommentSerializer, GetCommentsSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view


class CommentView(APIView):
    def post(self, request):
        product = request.data.get("product")
        content = request.data.get("content")
        parent_comment = request.data.get("parent_comment")
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


class GetCommentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        comment = Comment.objects.filter(product=pk).filter(
            parent_comment=None)
        data = GetCommentsSerializer(comment, many=True).data
        return Response({"data": data})

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.user.id == comment.user.id:
            comment.delete()
        else:
            raise PermissionDenied
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.user.id == comment.user.id:
            content = request.data.get("content")
            if content:
                comment.content = content
                comment.save()
            else:
                return Response({'error': 'Content must not empty'})
        else:
            raise PermissionDenied
        return Response(status=status.HTTP_200_OK)
