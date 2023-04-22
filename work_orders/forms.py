from django.forms import ModelForm
from .models import WorkOrder


class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['description', 'work_order_price', 'assigned_to', 'due_date', 'completed']
