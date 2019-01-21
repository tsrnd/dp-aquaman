from django.contrib import admin
from django.contrib.auth.backends import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
from yashoes.model import user_variant, category, comment, notification, product_category, product, rating, transaction_variant, transaction, variant
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('username', 'email', 'address', 'phone_number', 'image_profile', 'password1',
                   'password2'),
    }), )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'fields': ('address', 'phone_number', 'email', 'image_profile')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', )
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    search_fields = ('username', 'email')
    model = User
    list_display = ['email', 'username', 'is_superuser']


admin.site.register(User, CustomUserAdmin)
