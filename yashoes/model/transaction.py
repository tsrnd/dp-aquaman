from django.db import models
from django.conf import settings
from datetime import date, timedelta, datetime

class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=100)
    total = models.BigIntegerField()
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "transaction"
