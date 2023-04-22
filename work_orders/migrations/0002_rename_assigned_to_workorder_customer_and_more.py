# Generated by Django 4.1.5 on 2023-04-20 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='assigned_to',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='workorder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workorder_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workorder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]