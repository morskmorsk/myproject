from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart,
         name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('register/', views.register, name='register'),
    path('add_product/', views.add_product, name='add_product'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # Other URL patterns
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    # Other URL patterns
    path('my_orders/', views.user_orders, name='user_orders'),
    path('my_orders/<int:order_id>/', views.user_order_detail, name='user_order_detail'),
]
