from rest_framework import serializers
from yashoes.model.transaction import Transaction
from yashoes.models import User


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
