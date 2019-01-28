from django.db import models
from yashoes.model.brand import Brand


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    rate = models.FloatField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class ListProduct(object):
    def __init__(self, id, name, description, rate, image_link):
        self.id = id
        self.name = name
        self.description = description
        self.rate = rate
        self.image_link = image_link
