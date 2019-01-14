from django.db import models
from myapp.models import User

class Notification(models.Model):
    category = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_datetime = models.DateTimeField(blank=True)
    target_notification_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = "notification"
