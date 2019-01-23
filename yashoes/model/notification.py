from django.db import models
from django.conf import settings
from yashoes.model.comment import Comment
from yashoes.model.transaction import Transaction
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notify_datetime = models.DateTimeField(null=True, blank=True)
    notification_target_id = models.IntegerField(null=True, blank=True)
    notification_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        null=True, blank=True,
    )
    notification_target = GenericForeignKey(
        'notification_type',
        'notification_target_id',
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notification"
        