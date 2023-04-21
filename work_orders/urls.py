from django.urls import path
from .views import (workorder_list, create_workorder, workorder_detail,
                    update_workorder)

app_name = 'work_orders'

urlpatterns = [
    path('', workorder_list, name='workorder_list'),
    path('work_order/add/', create_workorder, name='create_workorder'),
    path('work_order/<int:pk>/', workorder_detail, name='workorder_detail'),
    path('work_order/<int:pk>/edit/', update_workorder, name='edit_workorder'),
]