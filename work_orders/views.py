from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import WorkOrder
from .forms import WorkOrderForm


@login_required
def workorder_list(request):
    workorders = WorkOrder.objects.all()
    return render(request, 'work_orders/workorder_list.html',
                  {'workorders': workorders})


@login_required
def workorder_detail(request, pk):
    workorder = get_object_or_404(WorkOrder, pk=pk, customer=request.user)
    return render(request, 'work_orders/workorder_detail.html',
                  {'workorder': workorder})
    

@login_required
def create_workorder(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            workorder = form.save(commit=False)
            workorder.customer = request.user
            workorder.created_by = request.user
            workorder.created_date = timezone.now()
            workorder.save()
            return redirect('work_orders:workorder_list')
    else:
        form = WorkOrderForm()
    return render(request, 'work_orders/workorder_form.html', {'form': form})


@login_required
def update_workorder(request, pk):
    workorder = get_object_or_404(WorkOrder, pk=pk, customer=request.user)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=workorder)
        if form.is_valid():
            workorder = form.save(commit=False)
            workorder.updated_by = request.user
            workorder.updated_date = timezone.now()
            workorder.save()
            return redirect('work_orders:workorder_list')
    else:
        form = WorkOrderForm(instance=workorder)
    return render(request, 'work_orders/update_workorder.html',
                  {'form': form, 'workorder': workorder})
