from rest_framework import serializers
from yashoes.model.variant import Variant


class ColorVariantSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField('query_count')

    def query_count(self, queryset):
        count = Variant.objects.raw('SELECT * FROM product as p INNER JOIN variant as v ON p.id = v.product_id WHERE color = %s', [queryset.color])
        return len(count)

    class Meta:
        model = Variant
        fields = ['color', 'count']