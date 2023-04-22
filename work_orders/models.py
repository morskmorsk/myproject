from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class WorkOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    work_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='workorder_assigned_to')
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='workorder_created_by',
                                   blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='workorder_updated_by',
                                   blank=True, null=True)

    def __str__(self):
        return self.description
