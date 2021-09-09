from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm, OrderFormMat

# Create your views here.


def checkout(request):
    """
    Renders the secure checkout view
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    order_form_mat = OrderFormMat()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'order_form_mat': order_form_mat
    }

    return render(request, template, context)
