from django import forms
from .models import ShoppingCartItem, Product

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/', null=True, blank=True)

#     def __str__(self):
#         return self.name


# class ShoppingCartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

class ShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['quantity', 'price']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Update fields based on your Product model
        fields = ['name', 'description', 'price', 'image']
