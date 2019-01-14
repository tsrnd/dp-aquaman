from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(min_length=3, validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    password = serializers.CharField(min_length=3)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def validate_password(self, value):
        pwdCF = 'password_confirm'
        if pwdCF not in self.initial_data or self.initial_data[pwdCF] != value:
            raise serializers.ValidationError('password not match')

    def create(self, valid_data):
        user = User(
            username=self.initial_data['username'],
            email=self.initial_data['email'],
        )
        user.set_password(self.initial_data['password'])
        user.save()
        return user
