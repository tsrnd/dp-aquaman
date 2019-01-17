from rest_framework import serializers
from yashoes.model.user_version import Cart
from ..model.version import Version


class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'version', 'quantity']

    def create(self, valid_data):
        return Cart.objects.create(**valid_data)
