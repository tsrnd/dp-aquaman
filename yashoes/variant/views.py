from rest_framework.response import Response
from rest_framework.views import APIView
from yashoes.model.variant import Variant
from yashoes.variant.serializers import ColorVariantSerializer


class ColorVariantAPIView(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        queryset = Variant.objects.all().distinct('color')
        serializer = ColorVariantSerializer(queryset, many=True)
        return Response({"result": serializer.data})
