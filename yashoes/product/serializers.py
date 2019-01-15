from rest_framework import serializers
from yashoes.model.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'rate']
