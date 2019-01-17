from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from yashoes.models import User
from rest_framework.utils import model_meta
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, min_length=3, validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    address = serializers.CharField(required=False)
    phone_number = serializers.CharField(max_length=10, required=False)
    image_profile = serializers.ImageField(required=False, validators= [FileExtensionValidator(allowed_extensions=['JPG', 'GIF', 'PNG', 'JPEG', 'TIFF'])])

    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'phone_number', 'image_profile']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance