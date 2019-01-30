from rest_framework.response import Response
from rest_framework.views import APIView
from yashoes.model.variant import Variant
from yashoes.variant.serializers import ColorVariantSerializer, SizeVariantSerializer


class ColorVariantAPIView(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        queryset = Variant.objects.all().distinct('color')
        serializer = ColorVariantSerializer(queryset, many=True)
        return Response({"result": serializer.data})


class SizeVariantAPIView(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        queryset = Variant.objects.all().distinct('size')
        serializer = SizeVariantSerializer(queryset, many=True)
        return Response({"result": serializer.data})
