from django.contrib import admin
from .models import Product, Membership, Collection

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'collection',
        'price',
        'image',
    )

    ordering = ('sku', )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'collection',
        'price',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Collection, CollectionAdmin)
