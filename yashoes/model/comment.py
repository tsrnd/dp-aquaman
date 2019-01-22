from django.db import models
from yashoes.model.product import Product
from django.conf import settings
from datetime import date, timedelta, datetime


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "comment"

    def soft_delete(self):
        date_time = datetime.now()
        self.deleted_at = date_time
        sub_comment = Comment.objects.filter(parent_comment=self.id).update(
            deleted_at=date_time)
        self.save()
