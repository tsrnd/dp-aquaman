from django.contrib import admin
from django.contrib.auth.backends import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
from django.contrib.auth.models import Group
from yashoes.model.product import Product
from yashoes.model.brand import Brand
from yashoes.model import user_variant, category, comment, notification, product_category, product, rating, transaction, variant
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib import admin
from yashoes.model.comment import Comment
from yashoes.model.transaction import Transaction, TransactionVariant




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
        return mark_safe('<img src="{url}" width="100px" height=100px />'.format(
            url = obj.image_profile.url,
            )
        )

class VariantInline(admin.StackedInline):
    model = variant.Variant
    extra = 0

    exclude = ('deleted_at', )

class VariantTransactionInLine(admin.TabularInline):
    model = Transaction.variants.through
    list_display = (
        'variant',
        'quantity',
        'price'
    )
    readonly_fields = [
        'variant',
        'quantity',
        'price',
    ]
    exclude = ('deleted_at',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'created_at')
    list_filter = ('brand', )
    exclude = ('rate', 'deleted_at')
    search_fields = ('name', 'brand__brand_name')

    inlines = [VariantInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'content', 'created_at')
    search_fields = ['product__name','user__username']
    list_filter = ('product__brand',)
    list_display_links = None

    def has_add_permission(self, request, obj=None):
        return False

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product Detail', {
            'fields': ('user', 'address', 'phone_number')
        }),
        ('Status', {
            'fields': ('total', 'status')
        }),
    )
    list_display = ('id','user', 'address', 'phone_number', 'total', 'status', 'created_at', 'updated_at')
    exclude = ('deleted_at',)
    list_filter = ('status', 'created_at')
    readonly_fields = [
        'user', 'address', 'phone_number', 'total'
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    inlines = [VariantTransactionInLine]

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'created_at')

admin.site.site_header = 'Yashoes Admin Dashboard'
admin.site.register(User, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Brand, BrandAdmin)
