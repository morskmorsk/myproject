# Generated by Django 4.1.5 on 2023-04-22 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0006_workorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='work_order_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
