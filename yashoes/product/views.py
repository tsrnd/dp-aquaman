from yashoes.model.product import Product, ListProduct
from yashoes.model.comment import Comment
from yashoes.product.serializers import ListProductSerializer, ProductDetailSerializer, GetCommentsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny

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
            for variant in product.variant_set.all():
                image_link = variant.image_link
                break
            tmp = ListProduct(product.id, product.name, product.description,
                              product.rate, image_link)
            response.append(tmp)

        serializer = ListProductSerializer(response, many=True)
        content = {
            'result_count': product_list.count(),
            'page': page,
            'next_page_flg': products.has_next(),
            'result': serializer.data,
        }
        return Response(content)


class ProductDetail(generics.RetrieveAPIView):
    permission_classes = ()

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailSerializer(instance=product)
        return Response(serializer.data)


class GetCommentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, product_id):
        comment = Comment.objects.filter(product=product_id).filter(
            parent_comment=None)
        data = GetCommentsSerializer(comment, many=True).data
        return Response({"data": data})
