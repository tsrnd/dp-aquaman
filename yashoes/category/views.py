from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from yashoes.category.serializer import CategorySerializer
from yashoes.model.category import Category
from yashoes.model.brand import Brand


class CategoryView(ViewSet):
    permission_classes = ()

    @staticmethod
    def list(request):
        brand_id = request.GET.get('brand_id')
        if brand_id:
            is_brand = True
            brand = Brand.objects.get(pk=brand_id)
            categories = Category.objects.filter(parent=None, name=brand.brand_name).order_by('id')
        else:
            is_brand = False
            categories = Category.objects.filter(parent=None).order_by('id')
        serializer = CategorySerializer(categories, many=True)
        data = { "categories": serializer.data }
        data["is_brand"] = is_brand
        return Response({"data": data}, status=status.HTTP_200_OK)
