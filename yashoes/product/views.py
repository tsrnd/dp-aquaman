from yashoes.model.product import Product
from yashoes.product.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


RESULT_LIMIT = 5


class Products(APIView):
    """
    A view that returns the count of products in JSON.
    """

    def get(self, request, format=None):
        product_list = Product.objects.all()

        page = request.GET.get('page', 1)
        result_limit = request.GET.get('result_limit', RESULT_LIMIT)

        paginator = Paginator(product_list, result_limit)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            page = paginator.num_pages
            products = paginator.page(page)

        serializer = ProductSerializer(products, many=True)
        content = {
            'result_count': product_list.count(),
            'page': page,
            'next_page_flg': products.has_next(),
            'result': serializer.data,
        }
        return Response(content)
