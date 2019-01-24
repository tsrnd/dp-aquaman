from rest_framework import serializers

from yashoes.model.user_variant import UserVariant


class UserVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVariant
        fields = ['user', 'variant', 'quantity']

    def create(self, valid_data):
        return UserVariant.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.quantity += int(self.initial_data['quantity'])
        instance.save()
        return instance


class CartSerializer(serializers.Serializer):
    variant_id = serializers.IntegerField()
    product_name = serializers.CharField(source='variant__product__name')
    quantity = serializers.IntegerField()
    price = serializers.IntegerField(source='variant__price')
    color = serializers.CharField(source='variant__color')
    size = serializers.IntegerField(source='variant__size')
    image_link = serializers.CharField(source='variant__image_link')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
