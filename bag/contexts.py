from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product
from discounts.models import Discount
from discounts.forms import DiscountApplyForm


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    discount_form = DiscountApplyForm()

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    discount_id = request.session.get('discount_id')

    if discount_id:
        discount = Discount.objects.get(id=discount_id)
        discount_percentage = discount.discount
        discount_effect = total * Decimal(discount.discount / 100)
    else:
        discount = None
        discount_effect = 0
        discount_percentage = None

    grand_total = delivery + total - discount_effect

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'discount_form': discount_form,
        'discount': discount_effect,
        'discount_percentage': discount_percentage,
        'grand_total': grand_total,
    }

    return context
