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

    product = Product.objects.get(pk=item_id)
    profile = UserProfile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url_wish')
 
    if profile.wish_list:

        # profile.wish_list.add_product(item_id)
        print(profile.wish_list)
    
    else:
        wish_list = WishList(user_profile=profile)
        profile.wish_list = wish_list
        profile.save()
        wish_list.add_product(product)

    messages.success(request, f'{product.card_name} added to your wish list.')

    return redirect('view_bag')
