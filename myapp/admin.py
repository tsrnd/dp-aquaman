from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User
from myapp.model import cart, category, comment, notification, product_category, product, rating, transaction_version, transaction, version


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_superuser']


admin.site.register(User, CustomUserAdmin)
