# Generated by Django 4.1.5 on 2023-04-20 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0002_rename_assigned_to_workorder_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='customer',
        ),
    ]