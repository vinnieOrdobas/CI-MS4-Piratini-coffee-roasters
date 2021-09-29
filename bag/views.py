from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    Renders the shopping bag view
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''
    Add a quantity of the specified product to the shopping bag
    '''

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.card_name} added to your bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    '''
    Adjust the quantity of the specified product
    '''

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    messages.info(request, f'{product.card_name} quantity adjusted.')
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    '''
    Remove the item from the shopping bag
    '''

    product = Product.objects.get(pk=item_id)

    try:

        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        messages.warning(request, f'{product.card_name}\
            removed from your bag.')
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
