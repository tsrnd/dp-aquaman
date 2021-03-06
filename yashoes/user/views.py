from yashoes.user.serializers import UpdateUserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from yashoes.models import User
import logging
from django.shortcuts import get_object_or_404

class UserView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    logger = logging.getLogger(__name__)

    @action(detail=False, methods=['PUT'], url_path='update-profile', url_name='update-profile')
    def update_user_detail(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        validator_data = UpdateUserSerializer(user, data=request.data)
        if not validator_data.is_valid():
            return Response(data=validator_data.errors, status=400)
        validator_data.save()
        return Response(data=validator_data.data, status=200)

    @action(detail=False, methods=['GET'], url_path='profile', url_name='profile')
    def get_user_detail(self, request, pk=None, deleted_at=None):
        user = get_object_or_404(User, pk=request.user.id)
        return Response(data={
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'address': user.address,
            'phone_number': user.phone_number,
            'image_profile': user.image_profile.name if not user.image_profile.name else user.image_profile.url,
        }, status=200)
