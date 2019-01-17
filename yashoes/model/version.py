from django.db import models
from yashoes.model.product import Product
import os


def get_image_path(instance, filename):
    return os.path.join('yashoes/static/product', str(instance.product.id),
                        filename)


class Version(models.Model):
    product = models.ForeignKey(
        Product, related_name='versions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=5, null=True, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=20, null=True, blank=True)
    image_link = models.ImageField(
        upload_to=get_image_path,
        default='yashoes/static/product/None/no-imgage.png',
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "version"
