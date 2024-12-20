# Generated by Django 5.0 on 2024-08-29 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.CreateModel(
            name='EventPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed')], default='Pending', max_length=20)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('event_registration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='events.eventregistration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
