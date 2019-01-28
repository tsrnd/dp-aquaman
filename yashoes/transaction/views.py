from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from yashoes.model.user_variant import UserVariant
from yashoes.model.variant import Variant
from .serializer import TransactionSerializer, TransactionVariantSerializer, VariantSerializer


class TransactionView(APIView):
    @staticmethod
    def post(request):
        request_data = request.data
        user_id = request.user.id
        try:
            transactions = get_cart(user_id)
        except ValidationError as e:
            return Response({'message': e.messages[0]}, status=status.HTTP_404_NOT_FOUND)
        address = request_data.get('address')
        phone_number = request_data.get('phone_number')
        total = get_total(transactions)
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
                delete_cart(user_id)
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_cart(user_id):
    transactions = UserVariant.objects.filter(user_id=user_id).values(
        'variant_id', 'quantity', 'variant__price'
    )
    if not transactions:
        raise ValidationError({'error': ['cart is empty.']})
    return transactions


def delete_cart(user_id):
    transactions = UserVariant.objects.filter(user_id=user_id)
    if transactions:
        transactions.delete()


def get_total(transactions):
    total = 0
    for trans in transactions:
        total += trans.get('variant__price') * trans.get('quantity')
    return total
