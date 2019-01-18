from yashoes.model.comment import Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status


class CommentView(APIView):
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user.id == comment.user.id:
            comment.delete()
        else:
            return Response({
                'error': "Can not delete comment of other user"
            },
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user.id == comment.user.id:
            content = request.data.get("content")
            if content:
                comment.content = content
                comment.save()
            else:
                return Response({'error': 'Content must not empty'})
        else:
            return Response({
                'error': "Can not edit comment of other user"
            },
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)