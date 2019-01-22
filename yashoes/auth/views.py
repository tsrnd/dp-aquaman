from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .serializer import RegisterSerializer
from django.shortcuts import get_object_or_404
from yashoes.models import User
import logging
from django.core.cache import cache


class AuthView(viewsets.ViewSet):

    permission_classes = ()
    logger = logging.getLogger(__name__)

    @action(
        detail=False,
        url_path='register',
        methods=['POST'],
        url_name='register')
    def register(self, request):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        try:
            validator_user = RegisterSerializer(data=request.data)
            if not validator_user.is_valid():
                return Response(data=validator_user.errors, status=400)
            payload = jwt_payload_handler(validator_user.save())
            token = jwt_encode_handler(payload)
            data_response = {
                'token': token,
            }
        except Exception as e:
            self.logger.error({
                'msg': 'has some error',
                'error': e,
            })
            return Response(status=500)
        self.logger.info({
            'msg': 'create user success',
            'status': 200
        })
        return Response(data=data_response, status=200)
