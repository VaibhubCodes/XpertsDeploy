# Generated by Django 5.0 on 2024-08-29 08:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0019_alter_payment_order_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='created_at',
            new_name='payment_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cohort',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.AddField(
            model_name='cohort',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 8, 55, 25, 730788, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='cohort',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 8, 55, 25, 730605, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='cohortregistration',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='payment',
            name='cohort_registration',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='cohorts.cohortregistration'),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cohortregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohort_registrations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
