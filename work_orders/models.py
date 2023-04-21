from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class WorkOrder(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
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
