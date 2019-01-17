from rest_framework import serializers
from yashoes.model.product import Product
from yashoes.model.variant import Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'name', 'size', 'color', 'price', 'quantity',
                  'image_link')


class ProductDetailSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField('is_variant_set')

    def is_variant_set(self, product):
        variant = Variant.objects.filter(product=product).order_by('id')
        serializers = VariantSerializer(variant, many=True)
        return serializers.data

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'rate', 'variants')


class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    rate = serializers.FloatField()
    image_link = serializers.CharField()
