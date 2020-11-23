from django import forms

from .models import InventoryWaitlist

class InventoryWaitlistForm(forms.ModelForm):
    def __init__(self, *args, **Kwargs):
        product = Kwargs.pop("product") or None
        super().__init__(*args, **Kwargs)
        self.product = product
    class Meta:
        model = InventoryWaitlist
        fields = [
            'email',
        ]


    def clean(self, *args, **Kwargs):
        cleaned_data = super().clean(*args, **Kwargs)
        #check product inventory
        email = cleaned_data.get("email")
        qs = InventoryWaitlist.objects.filter(product=self.product, email__iexact=email)
        if qs.count() > 5:
            error_msg = "10-4 we have your waitlist entry for this product"
            # raise self.add_error("email", error_msg)
            raise forms.ValidationError(error_msg) 
        

        return cleaned_data
