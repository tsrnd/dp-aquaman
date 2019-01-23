from yashoes.model.product import Product, ListProduct
from yashoes.model.variant import Variant
from yashoes.model.transaction import Transaction
from yashoes.model.rating import Rating
from yashoes.model.brand import Brand
from yashoes.product.serializers import ListProductSerializer, ProductDetailSerializer, GetCommentsSerializer, PostCommentSerializer, HomePageSerializer
from yashoes.rating.serializers import RatingSerializer
from yashoes.model.comment import Comment
from yashoes.product.response import HomePageResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from rest_framework import generics
from datetime import date, timedelta
from rest_framework import status
from django.db.models import Avg
from rest_framework.permissions import AllowAny
from datetime import date, timedelta, datetime

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


class RatingView(APIView):
    def post(self, request, product_id):
        rating = request.data.get("rating")
        user_id = request.user.id
        rating_range = range(1, 6)
        if rating:
            if int(rating) in rating_range:
                enddate = date.today()
                minimumdate = enddate - timedelta(days=7)
                variant_ids = list(
                    Variant.objects.filter(product=product_id).values_list(
                        'id', flat=True))
                transaction = Transaction.objects.filter(
                    user=user_id,
                    status=3,
                    transactionvariant__variant__in=variant_ids,
                    created_at__date__range=(minimumdate, enddate))
                if transaction:
                    data = {
                        'product': product_id,
                        'user': user_id,
                        'rate': rating
                    }
                    serializer = RatingSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        product = Product.objects.get(pk=product_id)
                        average_rating = Rating.objects.filter(
                            product=product_id).aggregate(
                                Avg('rate')).get('rate__avg')
                        product.rate = round(average_rating, 1)
                        product.save()
                        return Response({
                            "message": "success"
                        },
                                        status=status.HTTP_200_OK)
                    else:
                        return Response(
                            serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({
                        "error":
                        "Not found transaction with this product on last 7 days"
                    })
            else:
                return Response({"error": "Rating must in range [1-5]"})
        else:
            return Response({
                "error": "Rating is required"
            },
                            status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, product_id):
        comment = Comment.objects.filter(
            product=product_id, deleted_at=None).filter(parent_comment=None)
        data = GetCommentsSerializer(comment, many=True).data
        return Response({"data": data})

    def post(self, request, product_id):
        if request.user.is_authenticated:
            content = request.data.get("content")
            parent_comment = request.data.get("parent_comment_id")
            data = {
                'product': product_id,
                'content': content,
                'parent_comment': parent_comment
            }
            serializer = PostCommentSerializer(
                data=data, context={"user": request.user})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Login first"}, status=status.HTTP_401_UNAUTHORIZED)


class HomePageApiView(APIView):
    permission_classes = ()

    def get(self, request):
        """
        Get some product for home page
        With 1 brand will have 5 product
        """
        brands = Brand.objects.all().filter(deleted_at=None)[:5]

        response = []
        for brand in brands:
            products = Product.objects.filter(
                brand=brand.id, deleted_at=None)[:5]
            products_tmp = []
            for product in products:
                image_link = ""
                for variant in product.variant_set.all()[:1]:
                    image_link = variant.image_link
                    break
                tmp = ListProduct(product.id, product.name,
                                  product.description, product.rate,
                                  image_link)
                products_tmp.append(tmp)

            brand_tmp = HomePageResponse(brand.id, brand.brand_name,
                                         products_tmp)
            response.append(brand_tmp)

        serializers = HomePageSerializer(response, many=True)
        return Response({"result": serializers.data})
