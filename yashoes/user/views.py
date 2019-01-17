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

    @action(detail=False, methods=['PUT'], url_path='profile', url_name='profile')
    def update_user_detail(self, request, pk=None):
        user = get_object_or_404(User, pk=request.user.id)
        validator_data = UpdateUserSerializer(user, data=request.data)
        if not validator_data.is_valid():
            return Response(data=validator_data.errors, status=400)
        validator_data.save()
        return Response(data=validator_data.data, status=200)
