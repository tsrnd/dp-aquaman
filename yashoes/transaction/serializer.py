from rest_framework import serializers
from yashoes.model.transaction import Transaction
from yashoes.model.transaction_version import TransactionVersion
from yashoes.model.product import Product
from yashoes.model.version import Version

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
        fields = ('description', 'rate')
        # fields = '__all__'

class VersionSerializer(serializers.ModelSerializer):
    price = ProductSerializer(many=False, read_only =True)
    class Meta:
        model = Version
        fields = ('name', 'size', 'color', 'price')

class TransactionVersionSerializer(serializers.ModelSerializer):
    # product = serializers.IntegerField(source='version_id')
    # version = serializers.StringRelatedField(read_only=True)

    # version = serializers.SlugRelatedField()
    version = VersionSerializer(many=False, read_only=True)
    class Meta:
        model = TransactionVersion
        fields = ('quantity', 'version')
