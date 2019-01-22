from rest_framework import serializers
from yashoes.model.transaction import Transaction
from yashoes.model.transaction_variant import TransactionVariant
from yashoes.model.product import Product
from yashoes.model.variant import Variant

from yashoes.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('name', 'size', 'color', 'price', 'image_link',)

class TransactionVariantSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=False, read_only=True)
    class Meta:
        model = TransactionVariant
        fields = ('quantity','variant')


class TransactionSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source='id')
    class Meta:
        model = Transaction
        # fields = ('transaction_id','user_id','status','total','created_at')
        fields = '__all__'