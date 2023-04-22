from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ShoppingCartItem, Order
from .forms import ShoppingCartItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProductForm
from .forms import OrderCreateForm


@login_required
def user_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = ShoppingCartItem.objects.filter(order=order)
    return render(request, 'shop/user_order_detail.html', {'order': order, 'order_items': order_items})


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/user_orders.html', {'orders': orders})


@login_required
def order_success(request):
    return render(request, 'shop/order_success.html')


@login_required
def checkout(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user, order=None)

    if not cart_items:
        return redirect('shop:view_cart')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for cart_item in cart_items:
                cart_item.order = order
                cart_item.save()

            # Redirect to a payment process or a success page
            return redirect('shop:order_success')

    else:
        form = OrderCreateForm()

    return render(request, 'shop/checkout.html', {'form': form, 'cart_items': cart_items})



@login_required
def profile(request, username):
    return render(request, 'accounts/profile.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration.
            login(request, user)
            # Redirect to your desired page after registration
            return redirect('shop:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = ShoppingCartItem.objects.get_or_create(
#         user=request.user,
#         product=product,
#         defaults={
#             'shopping_cart_item_price': product.product_price,
#             'quantity': 1,
#         }
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect('shop:view_cart')


# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = ShoppingCartItem.objects.get_or_create(
#         user=request.user,
#         product=product,
#         defaults={
#             'shopping_cart_item_price': product.product_price,
#             'quantity': 1,
#         }
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     print("DEBUG: Cart Item Order:", cart_item.order)  # Debug print

#     return redirect('shop:view_cart')


# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = ShoppingCartItem.objects.get_or_create(
#         user=request.user,
#         product=product,
#         defaults={
#             'shopping_cart_item_price': product.product_price,
#             'quantity': 1,
#         }
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     # Add this print statement
#     print(f"DEBUG: Cart Item Order: {cart_item.order}")

#     return redirect('shop:view_cart')


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = ShoppingCartItem.objects.get_or_create(
        user=request.user,
        product=product,
        order=None,  # Add this line
        defaults={
            'shopping_cart_item_price': product.product_price,
            'quantity': 1,
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shop:view_cart')


@login_required
def view_cart(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user, order=None)
    print("DEBUG: Cart Items:", cart_items)  # Debug print
    cart_total = sum(item.total_price for item in cart_items)
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items, 'cart_total': cart_total})


@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id)
    form = ShoppingCartItemForm(request.POST or None, instance=cart_item)

    if form.is_valid():
        form.save()
        cart_item.refresh_from_db()  # Refresh the cart_item instance to get the updated quantity

        print("DEBUG: Product price:", cart_item.product.product_price)  # Debug print
        print("DEBUG: Updated quantity:", cart_item.quantity)  # Debug print

        cart_item.cart_item_price = cart_item.product.product_price * cart_item.quantity
        cart_item.save()

        print("DEBUG: Updated price:", cart_item.cart_item_price)  # Debug print

        return redirect('shop:view_cart')

    return render(request, 'shop/update_cart.html',
                  {'form': form, 'cart_item': cart_item})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id)
    cart_item.delete()
    return redirect('shop:view_cart')
