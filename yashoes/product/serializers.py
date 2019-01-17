from rest_framework import serializers
from yashoes.model.product import Product
from yashoes.model.version import Version


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('id', 'name', 'size', 'color', 'price', 'quantity',
                  'image_link')


class ProductDetailSerializer(serializers.ModelSerializer):
    versions = VersionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'rate', 'versions')


class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    rate = serializers.FloatField()
    image_link = serializers.CharField()
