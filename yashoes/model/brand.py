from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = "brand"
