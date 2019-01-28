from rest_framework import serializers
from yashoes.model.variant import Variant
from yashoes.model.product import Product
from yashoes.models import User
from yashoes.model.transaction import Transaction, TransactionVariant


class TransactionSerializer(serializers.Serializer):
    def get_status_as_char(self, obj):
       return  obj.get_status_display()
    user_id = serializers.IntegerField()
    transaction_id = serializers.IntegerField(source='id')
    product = serializers.CharField(source='name')
    status = serializers.SerializerMethodField("get_status_as_char")
    address = serializers.CharField()
    total = serializers.IntegerField()
    phone_number = serializers.IntegerField()
    created_at = serializers.DateTimeField(format='%H:%M %d %b %Y')

class DetailVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('name', 'size', 'color', 'price', 'image_link',)
class TransactionDetailSerializer(serializers.ModelSerializer):
    variant = DetailVariantSerializer(many=False, read_only=True)
    class Meta:
        model = TransactionVariant
        fields = ('id','quantity','variant')
