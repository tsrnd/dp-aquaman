from yashoes.model.product import Product, ListProduct
from yashoes.product.serializers import ListProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


RESULT_LIMIT = 5


class ProductsAPIView(APIView):
    """
    A view that returns the list of products in JSON.
    """
    permission_classes = ()

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

        response = []
        for product in products:
            image_link = ""
            for version in product.versions.all():
                image_link = version.image_link
                break
            tmp = ListProduct(
                product.id,
                product.name,
                product.description,
                product.rate,
                image_link)
            response.append(tmp)

        serializer = ListProductSerializer(response, many=True)
        content = {
            'result_count': product_list.count(),
            'page': page,
            'next_page_flg': products.has_next(),
            'result': serializer.data,
        }
        return Response(content)
