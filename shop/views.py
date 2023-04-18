from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ShoppingCartItem
from .forms import ShoppingCartItemForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = ShoppingCartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop:product_list')


@login_required
def view_cart(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user)
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items})


@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id)
    form = ShoppingCartItemForm(request.POST or None, instance=cart_item)
    if form.is_valid():
        form.save()
        return redirect('shop:view_cart')
    return render(request, 'shop/update_cart.html', {'form': form, 'cart_item': cart_item})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id)
    cart_item.delete()
    return redirect('shop:view_cart')
