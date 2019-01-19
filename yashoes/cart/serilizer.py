from rest_framework import serializers
from yashoes.model.user_variant import UserVariant


class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserVariant
        fields = ['user', 'variant', 'quantity']

    def create(self, valid_data):
        return UserVariant.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.quantity += self.initial_data['quantity']
        instance.save()
        return instance
