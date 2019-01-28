from rest_framework import serializers
from yashoes.model.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'