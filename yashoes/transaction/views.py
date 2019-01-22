from rest_framework.response import Response
from yashoes.models import User
from rest_framework import viewsets
from .serializer import TransactionSerializer
from .serializer import TransactionVariantSerializer
from yashoes.model.transaction import Transaction
from yashoes.model.product import Product
from yashoes.model.variant import Variant

from yashoes.model.transaction_variant import TransactionVariant
from django.shortcuts import get_object_or_404
from datetime import date, timedelta, datetime

class TransactionView(viewsets.ViewSet):
    def list(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        queryset = Transaction.objects.filter(user_id=user).exclude(deleted_at__isnull=False)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=request.user.id)
        transaction = TransactionVariant.objects.filter(transaction__pk=pk).filter(transaction__user_id=user).exclude(deleted_at__isnull=False)
        serializer = TransactionVariantSerializer(transaction, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        # transaction_id = TransactionVariant.objects.filter(transaction__pk=transactionvariant.transaction__pk)
        # transaction_variant = TransactionVariant.objects.select_related('transaction').get(id=1)
        # print("hihihhihiihihi",transaction_variant)

        date_time = datetime.now()
        user = get_object_or_404(User, pk=request.user.id)
        transaction = TransactionVariant.objects.filter(transaction__pk=pk).update(deleted_at=date_time)
        transaction = Transaction.objects.filter(id=pk).update(deleted_at=date_time)
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data, many=True)