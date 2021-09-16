from django.shortcuts import render, redirect, reverse
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
    redirect_url = request.POST.get('url')

    if profile.wish_list.exists():
        wish_list = profile.wish_list.get()
        if product in wish_list.products.all():
            messages.warning(request, f'{product.card_name} already on your wish list!')
        else:
            wish_list.products.add(product)
            messages.success(request, f'{product.card_name} added to your wish list.')

    else:
        wish_list = WishList(user_profile=profile)
        wish_list.save()
        wish_list.products.add(product)
        messages.success(request, f'{product.card_name} added to your wish list.')

    return redirect(redirect_url)


def remove_from_wish_list(request, item_id):
    """
    Deletes product from the wish_list
    """

    profile = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(pk=item_id)

    wish_list = profile.wish_list.get()
    wish_list.products.remove(product)
    wish_list.save()

    messages.success(request, f'{product.card_name} removed from your wish list.')

    return redirect(reverse('profile'))

