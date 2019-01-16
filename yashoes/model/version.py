from django.db import models
from yashoes.model.product import Product


class Version(models.Model):
    product = models.ForeignKey(
        Product, related_name='versions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=5, null=True, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=20, null=True, blank=True)
    image_link = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "version"
