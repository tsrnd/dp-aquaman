from rest_framework.response import Response
from yashoes.models import User
from rest_framework import viewsets
from .serializer import TransactionSerializer
from yashoes.model.transaction import Transaction
from rest_framework.authentication import get_authorization_header
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated


jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class Transaction_detailView(viewsets.ViewSet):
    def list(self, request):
        token = get_authorization_header(request)
        trulyToken = token.split()[1].decode('utf-8')
        user_information = jwt_decode_handler(trulyToken)
        print("AHIHIHIHIHIHI", user_information.get('address'))
        queryset = Transaction.objects.filter(user_id = user_information.get('user_id'))
        serializer = TransactionSerializer(queryset, context={'fields': ['user_id','address','phone_number','status','total']}, many=True)
        return Response(serializer.data, status=200)
