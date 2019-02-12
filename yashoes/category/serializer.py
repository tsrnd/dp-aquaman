from rest_framework import serializers

from yashoes.model.category import Category
from yashoes.model.brand import Brand


class CategorySerializer(serializers.ModelSerializer):
    brand_id = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField('get_sub_category')

    class Meta:
        model = Category
        fields = ('id', 'name', 'brand_id', 'sub_categories')

    @staticmethod
    def get_sub_category(category):
        categories = Category.objects.filter(parent=category.id).order_by('id')
        serializer = SubCategorySerializer(categories, many=True)
        return serializer.data

    @staticmethod
    def get_brand_id(category):
        try:
            brand = Brand.objects.get(brand_name=category.name)
            return brand.id
        except Brand.DoesNotExist:
            return None


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
