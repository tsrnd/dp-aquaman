from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = "product"
