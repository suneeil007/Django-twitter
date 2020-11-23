from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **Kwargs):
        product = Kwargs.pop("product") or None
        super().__init__(*args, **Kwargs)
        self.product = product
    class Meta:
        model = Order
        fields = [
            'shipping_address',
            'billing_address',
        ]

    def clean(self, *args, **Kwargs):
        cleaned_data = super().clean(*args, **Kwargs)
        #check product inventory
        if self.product != None:
            if not self.product.can_order:
                raise forms.ValidationError("This product cannot be ordered at this time.")
        return cleaned_data
