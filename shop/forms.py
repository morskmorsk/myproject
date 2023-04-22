from django import forms
from .models import ShoppingCartItem, Product
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

class ShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['quantity', 'shopping_cart_item_price']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Update fields based on your Product model
        fields = ['name', 'description', 'product_price', 'image']
