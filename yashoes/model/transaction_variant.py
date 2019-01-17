from django.db import models
from yashoes.model.transaction import Transaction
from yashoes.model.variant import Variant


class TransactionVariant(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "transaction_variant"
