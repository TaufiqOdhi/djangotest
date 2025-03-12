from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['deleted_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full border border-gray-300 p-2 rounded'})

    def prefill(self, product):
        for field in self.fields:
            self.fields[field].initial = getattr(product, field)
