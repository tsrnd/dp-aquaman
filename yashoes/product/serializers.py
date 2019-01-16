from rest_framework import serializers
from yashoes.model.product import Product


class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    rate = serializers.FloatField()
    image_link = serializers.CharField()
