from rest_framework import serializers

from yashoes.model.user_variant import UserVariant


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVariant
        fields = ['user', 'variant', 'quantity']

    def create(self, valid_data):
        return UserVariant.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.quantity += int(self.initial_data['quantity'])
        instance.save()
        return instance


class CartSerializer1(serializers.Serializer):
    id = serializers.IntegerField(source='variant_id')
    product_name = serializers.CharField(source='variant__product__name')
    quantity = serializers.IntegerField(source='variant__quantity')
    image_link = serializers.CharField(source='variant__image_link')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
