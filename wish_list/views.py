from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import WishList
from products.models import Product
from profiles.models import UserProfile


@require_POST
def add_to_wish_list(request, item_id):
    """
    Add a product to the wishlist
    """

    profile = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(pk=item_id)

    if profile.wish_list.exists():
        wish_list = profile.wish_list.get()
        if product in wish_list.products.all():
            messages.warning(request, f'{product.card_name} already on your wish list!')
        else:
            wish_list.products.add(product)

    else:  
        wish_list = WishList(user_profile=profile)
        wish_list.save()
        wish_list.products.add(product)

    for product in wish_list.products.all():
        print(product.name)

    messages.success(request, f'{product.card_name} added to your wish list.')

    return redirect('view_bag')
