from django.db import models

from profiles.models import UserProfile
from products.models import Product

# Create your models here.


class WishList(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name="wish_list")
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f'{self.user_profile} Wishlist'

    def add_product(self,item_id):
        product = Product.objects.get(pk=item_id)
        
        self.products.add(product)
        self.save()
