from rest_framework import serializers
from yashoes.model.brand import Brand


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name']
