from django.db import models
from myapp.models import User
from myapp.model.version import Version
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE) 
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = "cart"
