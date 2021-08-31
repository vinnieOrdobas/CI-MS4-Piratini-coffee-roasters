from django.contrib import admin
from .models import Product, Membership, Collection

# Register your models here.
admin.site.register(Product)
admin.site.register(Membership)
admin.site.register(Collection)
