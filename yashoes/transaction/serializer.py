from rest_framework import serializers
from yashoes.model.product import Product
from yashoes.model.variant import Variant
from yashoes.models import User
from yashoes.model.transaction import Transaction, TransactionVariant

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('name', 'size', 'color', 'price', 'image_link',)

class TransactionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionVariant
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['quantity']

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity')
        instance.save()
        return instance

class TransactionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    transaction_id = serializers.IntegerField(source='id')
    product = serializers.CharField(source='name')
    status =  serializers.CharField()
    address = serializers.CharField()
    total = serializers.IntegerField()
    phone_number = serializers.IntegerField()
    created_at = serializers.DateTimeField()

class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names
        return super(FieldMixin, self).get_field_names(*args, **kwargs)

class TransactionCreateSerializer(FieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
