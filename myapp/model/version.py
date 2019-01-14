from django.db import models
from myapp.model.product import Product

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=5)
    price = models.IntegerField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=20)
    image_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = "version"