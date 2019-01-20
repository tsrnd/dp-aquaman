from rest_framework import serializers
from yashoes.model.transaction import Transaction
from yashoes.model.transaction_variant import TransactionVariant
from yashoes.model.product import Product
from yashoes.model.variant import Variant

from yashoes.models import User


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names
        return super(FieldMixin, self).get_field_names(*args, **kwargs)

class TransactionSerializer(FieldMixin, serializers.ModelSerializer, object):
    transaction_id = serializers.IntegerField(source='id')
    class Meta:
        model = Transaction
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('rate','description')

class VariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only =True)
    class Meta:
        model = Variant
        fields = ('name', 'size', 'color', 'product', 'price')

class TransactionVariantSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source='variant_id')
    variant = VariantSerializer(many=False, read_only=True)
    class Meta:
        model = TransactionVariant
        fields = ('transaction_id', 'quantity', 'variant')
