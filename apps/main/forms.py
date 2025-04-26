from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'image', 
            'category',
            'available_size',
            'color',
            'price'
        ]
        labels = {
            "image": "Image",
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["payment_method", "total_amount"]