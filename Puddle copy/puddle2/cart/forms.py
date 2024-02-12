from django import forms
from django.core.validators import validate_slug
from .models import *

class ApplyDiscountForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['discount_code']
        labels = {'discount_code': 'Discount Code'}