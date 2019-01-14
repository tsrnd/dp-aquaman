from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "user"