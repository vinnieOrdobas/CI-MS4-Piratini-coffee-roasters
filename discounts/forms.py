from django import forms
from .models import Discount


class DiscountApplyForm(forms.Form):
    code = forms.CharField(required=False)

class DiscountForm(forms.ModelForm):

    class Meta:
        model = Discount
        fields = '__all__'
