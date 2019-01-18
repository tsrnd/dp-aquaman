from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from yashoes.model.brand import Brand
from yashoes.brand.serializers import BrandSerializers


class BrandViewSet(viewsets.ViewSet):
    permission_classes = ()

    @action(detail=False, url_path='brands', url_name='brand_index')
    def index(self, request):
        queryset = Brand.objects.all().filter(deleted_at=None)
        serializers = BrandSerializers(queryset, many=True)
        return Response({"result": serializers.data})

    # @action(detail=False, url_path='brands/(?P<pk>[0-9]+)', url_name='brand_index')
    # def get_product(self, request, pk=None):
    #     queryset = Brand.objects.all().filter(pk=pk, deleted_at=None)
    #     serializers = BrandSerializers(queryset, many=True)
    #     print("======this is api home page ========", pk)
    #     return Response({"data": serializers.data})
