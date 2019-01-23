from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from yashoes.model.transaction import Transaction, TransactionVariant
from yashoes.model.variant import Variant
from .serializer import TransactionSerializer, TransactionVariantSerializer, VariantSerializer, TransactionCreateSerializer


from .serializer import TransactionSerializer
from .serializer import TransactionVariantSerializer
from yashoes.model.transaction import Transaction
from yashoes.model.product import Product
from yashoes.model.variant import Variant
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from yashoes.models import User


class TransactionViews(viewsets.ViewSet):
    def list(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        queryset = Transaction.objects.raw("SELECT product.name, transaction.* from product inner join variant on product.id = variant.product_id inner join transactions_variants on variant.id = transactions_variants.variant_id inner join transaction on transactions_variants.transaction_id = transaction.id")
        print("phutran", queryset)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=request.user.id)
        transaction = TransactionVariant.objects.filter(transaction__pk=pk).filter(transaction__user_id=user)
        serializer = TransactionVariantSerializer(transaction, many=True)
        return Response(serializer.data)

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
        serializer = TransactionCreateSerializer(data=data)
        with transaction.atomic():
            sid = transaction.savepoint()
            if serializer.is_valid():
                serializer.save()
                transaction_id = serializer.data.get('id')
                for trans in transactions:
                    variant_id = trans.get('variant_id')
                    quantity = trans.get('quantity')
                    variant = get_object_or_404(Variant, pk=variant_id)
                    if variant.quantity >= quantity:
                        variant_data = {
                            'quantity': variant.quantity - quantity
                        }
                        variant_serializer = VariantSerializer(variant, data=variant_data)
                        if variant_serializer.is_valid():
                            variant_serializer.save()
                        else:
                            transaction.savepoint_rollback(sid)
                            return Response(variant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        tv_data = {
                            'quantity': quantity,
                            'variant': variant_id,
                            'transaction': transaction_id
                        }
                        tv_serializer = TransactionVariantSerializer(data=tv_data)
                        if tv_serializer.is_valid():
                            tv_serializer.save()
                        else:
                            transaction.savepoint_rollback(sid)
                            return Response(tv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        transaction.savepoint_rollback(sid)
                        return Response({'variant_id': variant_id, 'message': 'quantity not enough'},
                                        status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
