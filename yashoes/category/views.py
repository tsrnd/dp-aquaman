from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from yashoes.category.serializer import CategorySerializer
from yashoes.model.category import Category


class CategoryView(ViewSet):
    permission_classes = ()

    @staticmethod
    def list(request):
        categories = Category.objects.filter(parent=None).order_by('id')
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
