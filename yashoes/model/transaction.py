from django.db import models
from django.conf import settings
from datetime import date, timedelta, datetime

class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    status_choices = (
        (1, 'in processing'),
        (2, 'in delivery'),
        (3, 'done'),
        (4, 'cancel'),
    )
    status = models.CharField(max_length=1, choices=status_choices)
    total = models.BigIntegerField()
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "transaction"
