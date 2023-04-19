from django import forms
from .models import ShoppingCartItem, Product


class ShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['quantity']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Update fields based on your Product model
        fields = ['name', 'description', 'price', 'image']
