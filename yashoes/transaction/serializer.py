from rest_framework import serializers
from yashoes.model.transaction import Transaction
from yashoes.model.transaction_variant import TransactionVariant
from yashoes.model.product import Product
from yashoes.model.variant import Variant
from yashoes.models import User

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('name', 'size', 'color', 'price', 'image_link',)

class TransactionVariantSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=False, read_only=True)
    class Meta:
        model = TransactionVariant
        fields = ('quantity','variant')

class TransactionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    transaction_id = serializers.IntegerField(source='id')
    product = serializers.CharField(source='name')
    status =  serializers.CharField()
    address = serializers.CharField()
    total = serializers.IntegerField()
    phone_number = serializers.IntegerField()
    created_at = serializers.DateTimeField()
