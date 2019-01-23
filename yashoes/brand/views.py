from rest_framework.response import Response
from rest_framework.views import APIView
from yashoes.model.brand import Brand
from yashoes.brand.serializers import BrandSerializer

RESULT_LIMIT = 5


class BrandAPIView(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        result_limit = request.GET.get('result_limit', RESULT_LIMIT)
        queryset = Brand.objects.all().only("brand_name")[:RESULT_LIMIT]
        serializer = BrandSerializer(queryset, many=True)
        return Response({"result": serializer.data})
