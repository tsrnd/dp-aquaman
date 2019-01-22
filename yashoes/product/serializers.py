from rest_framework import serializers
from yashoes.model.product import Product
from yashoes.model.variant import Variant
from yashoes.model.comment import Comment
from yashoes.model.brand import Brand


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'name', 'size', 'color', 'price', 'quantity',
                  'image_link')


class ProductDetailSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField('is_variant_set')

    def is_variant_set(self, product):
        variant = Variant.objects.filter(product=product).order_by('id')
        serializers = VariantSerializer(variant, many=True)
        return serializers.data

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'rate', 'variants')


class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    rate = serializers.FloatField()
    image_link = serializers.CharField()


class SubCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    created_at = serializers.DateTimeField(format='%H:%M %d %b %Y')
    user_image = serializers.CharField(source='user.image_profile.url')

    class Meta:
        model = Comment
        fields = ('id', 'username', 'user_image', 'content', 'created_at')


class GetCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('query_comments')
    username = serializers.CharField(source='user.username')
    created_at = serializers.DateTimeField(format='%H:%M %d %b %Y')
    user_image = serializers.CharField(source='user.image_profile.url')


    def query_comments(self, comment):
        comments = Comment.objects.filter(parent_comment=comment.id)
        serializers = SubCommentSerializer(comments, many=True)
        return serializers.data

    class Meta:
        model = Comment
        fields = ('id', 'username', 'user_image', 'content', 'comments',
                  'created_at')


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'product', 'parent_comment')

    def create(self, validated_data):
        user = self.context.get("user")
        product = validated_data['product']
        content = validated_data['content']
        parent_comment = validated_data['parent_comment']
        comment = Comment(
            product=product, content=content, parent_comment=parent_comment)
        comment.user = user
        comment.save()
        return comment


class HomePageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    brand_name = serializers.CharField()
    products = ListProductSerializer(many=True)
