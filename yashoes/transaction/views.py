from django.db import transaction
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from yashoes.model.transaction import Transaction
from .serializer import TransactionSerializer, TransactionVariantSerializer

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class Transaction_detailView(viewsets.ViewSet):
    def list(self, request):
        token = get_authorization_header(request)
        trulyToken = token.split()[1].decode('utf-8')
        user_information = jwt_decode_handler(trulyToken)
        queryset = Transaction.objects.filter(user_id=user_information.get('user_id'))
        serializer = TransactionSerializer(queryset, context={
            'fields': ['user_id', 'address', 'phone_number', 'status', 'total']}, many=True)
        return Response(serializer.data, status=200)


class TransactionView(APIView):
    @staticmethod
    def post(request):
        request_data = request.data
        user_id = request.user.id
        transactions = request_data.get('transactions')
        address = request_data.get('address')
        phone_number = request_data.get('phone_number')
        total = request_data.get('total')
        data = {
            'user': user_id,
            'address': address,
            'phone_number': phone_number,
            'total': total,
            'status': 1
        }
        serializer = TransactionSerializer(data=data)
        with transaction.atomic():
            sid = transaction.savepoint()
            if serializer.is_valid():
                serializer.save()
                transaction_id = serializer.data.get('id')
                for trans in transactions:
                    tv_data = {
                        'quantity': trans.get('quantity'),
                        'variant': trans.get('variant_id'),
                        'transaction': transaction_id
                    }
                    tv_serializer = TransactionVariantSerializer(data=tv_data)
                    if tv_serializer.is_valid():
                        tv_serializer.save()
                    else:
                        transaction.savepoint_rollback(sid)
                        return Response(tv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
