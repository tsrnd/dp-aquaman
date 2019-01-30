from django.db import models
from yashoes.model.product import Product
import os


def get_image_path(instance, filename):
    return os.path.join('products', str(instance.product.id),
                        filename)


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=5, null=True, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=20, null=True, blank=True)
    image_link = models.ImageField(
        upload_to=get_image_path,
        blank=True,
        null=True,
        max_length=50000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def _get_image_link_url(self):
        image_link = 'image_not_found'
        if self.image_link == '':
            if "http" in self.image_link.name:
                image_link = self.image_link
            else:
                image_link = self.image_link.name if not self.image_link.name else self.image_link.url
        return image_link

    image_link_url = property(_get_image_link_url)

    class Meta:
        db_table = "variant"
