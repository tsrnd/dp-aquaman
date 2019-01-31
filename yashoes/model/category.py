from django.db import models


class CategoryManager(models.Manager):
    def is_empty(self):
        return


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
