from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from yashoes.model.transaction import Transaction, TransactionVariant
from yashoes.models import User
from .serializer import TransactionSerializer, TransactionDetailSerializer


class TransactionViews(viewsets.ViewSet):
    def list(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        queryset = Transaction.objects.raw(
            "SELECT product.name, transaction.* from product inner join variant on product.id = variant.product_id "
            "inner join transactions_variants on variant.id = transactions_variants.variant_id "
            "inner join transaction on transactions_variants.transaction_id = transaction.id where user_id=%s",
            [user.id])
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=request.user.id)
        transaction = TransactionVariant.objects.filter(transaction__pk=pk).filter(transaction__user_id=user)
        serializer = TransactionDetailSerializer(transaction, many=True)
        return Response(serializer.data)
