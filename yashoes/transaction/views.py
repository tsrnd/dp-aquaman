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

class Transaction_listlView(viewsets.ViewSet):
    def list(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        queryset = Transaction.objects.filter(user_id = user).exclude(deleted_at__isnull = False)
        serializer = TransactionSerializer(queryset, context={'fields': ['transaction_id','user_id','address','phone_number','status','total']}, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=request.user.id)
        transaction = TransactionVariant.objects.filter(transaction__pk = pk).filter(transaction__user_id = user)
        serializer = TransactionVariantSerializer(transaction, many=True)
        return Response(serializer.data)
