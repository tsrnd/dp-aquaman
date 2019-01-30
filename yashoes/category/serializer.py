from rest_framework import serializers

from yashoes.model.category import Category


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField('get_sub_category')

    class Meta:
        model = Category
        fields = ('id', 'name', 'sub_categories')

    @staticmethod
    def get_sub_category(category):
        categories = Category.objects.filter(parent=category.id).order_by('id')
        serializer = SubCategorySerializer(categories, many=True)
        return serializer.data


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
