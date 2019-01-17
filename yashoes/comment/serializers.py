from rest_framework import serializers
from yashoes.model.comment import Comment
from yashoes.model.product import Product


class SubCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'username', 'content', 'created_at')


class GetCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('query_comments')
    username = serializers.CharField(source='user.username')

    def query_comments(self, comment):
        comments = Comment.objects.filter(parent_comment=comment.id)
        serializers = SubCommentSerializer(comments, many=True)
        return serializers.data

    class Meta:
        model = Comment
        fields = ('id', 'username', 'content', 'comments', 'created_at')


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
