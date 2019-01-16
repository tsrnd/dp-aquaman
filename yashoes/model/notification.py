from django.db import models
from django.conf import settings
from yashoes.model.comment import Comment
from yashoes.model.transaction import Transaction


class Notification(models.Model):
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notify_datetime = models.DateTimeField(null=True, blank=True)
    comments = models.ManyToManyField(Comment)
    transactions = models.ManyToManyField(Transaction)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notification"
        