from django.db import models
from yashoes.model.transaction import Transaction
from yashoes.model.version import Version


class TransactionVersion(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "transaction_version"
