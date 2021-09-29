from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Discount
from .forms import DiscountApplyForm

import datetime


@require_POST
def discount_apply(request):
    now = datetime.datetime.now()
    form = DiscountApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            discount = Discount.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True)
            request.session['discount_id'] = discount.id
            messages.success(request, f'{discount.code} applied to your bag.')
        except Discount.DoesNotExist:
            request.session['discount_id'] = None
            messages.error(request, 'Discount code does not exist or is not\
                                     valid anymore.')
    return redirect('view_bag')
