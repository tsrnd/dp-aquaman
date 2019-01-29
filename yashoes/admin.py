from django.contrib import admin
from django.contrib.auth.backends import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
from django.contrib.auth.models import Group
from yashoes.model.product import Product
from yashoes.model import user_variant, category, comment, notification, product_category, product, rating, transaction, variant
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class CustomUserAdmin(UserAdmin):
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields':
        ('username', 'email', 'address', 'phone_number', 'image_profile',
         'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
    }), )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'fields': ('email', 'image_profile_link', 'image_profile')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {
            'fields': ('last_login', )
        }),
    )
    readonly_fields = ['image_profile_link']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    search_fields = ('username', 'email')
    model = User
    list_display = ['email', 'username', 'is_superuser']

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if obj.is_superuser == False:
            return (
                (None, {
                    'fields': ('username', 'password')
                }),
                (_('Personal info'), {
                    'fields': ('address', 'phone_number', 'email',
                               'image_profile_link', 'image_profile')
                }),
                (_('Permissions'), {
                    'fields': ('is_active', 'is_staff', 'is_superuser')
                }),
            )
        return self.fieldsets

    def image_profile_link(self, obj):
        return mark_safe(
            '<img src="{url}" width="100px" height=100px />'.format(
                url=obj.image_profile.url, ))


class VariantInline(admin.StackedInline):
    model = variant.Variant
    extra = 0

    exclude = ('deleted_at', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'created_at')
    list_filter = ('brand', )
    exclude = ('rate', 'deleted_at')

    search_fields = ('name', 'brand__brand_name')

    inlines = [VariantInline]


admin.site.site_header = 'Yashoes Admin Dashboard'
admin.site.register(User, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
