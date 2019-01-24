from rest_framework import serializers

from yashoes.model.transaction import Transaction, TransactionVariant
from yashoes.model.variant import Variant


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names
        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class TransactionSerializer(FieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


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
