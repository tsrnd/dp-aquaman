from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .serializer import RegisterSerializer
from django.contrib.sites.shortcuts import get_current_site
import logging
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from smtplib import SMTPException
from rest_framework import status
from celery import shared_task
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
import datetime


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
            user = validator_user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            data_response = {
                'token': token,
            }
            # define mail content
            try:
                site = str(get_current_site(request))
                username = user.username
                email = user.email
                pk = user.pk
                u = get_user_model()()
                test = jwt_payload_handler(u)
                tk = jwt_encode_handler(test)
                print("THATSHOULD", tk)
                send_mail.s(pk, username, email, site).apply_async()
            except SMTPException:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            self.logger.error({
                'msg': 'has some error',
                'error': e,
            })
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.logger.info({
            'msg': 'create user success',
            'status': status.HTTP_200_OK
        })
        return Response(data=data_response, status=200)

    @action(detail=False, methods=['POST'], url_path='activate', url_name='activate')
    def activate_account(self, request):
        uid = request.data.get('uid')
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            user = get_user_model().objects.get(pk=uid)
            user.is_active = True
            user.save()
        except get_user_model().DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=200)


@shared_task
def send_mail(pk, username, email, site):
    subject = 'Active account mail'
    content = render_to_string('mail/active_mail_template.html', {
        'username': username,
        'domain': site,
        'user_id': urlsafe_base64_encode(force_bytes(pk)).decode(),
    })
    active_mail = EmailMessage(subject, content, to=[email])
    active_mail.send()
