from rest_framework import serializers
from yashoes.models import User
from yashoes.model.remind import Remind
from yashoes.model.variant import Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class RemindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remind
        fields = '__all__'
    
    def create(self, validated_data):
        return Remind.objects.create(**validated_data)
