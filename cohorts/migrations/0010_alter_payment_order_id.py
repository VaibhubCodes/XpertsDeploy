# Generated by Django 5.0 on 2024-08-28 16:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0009_alter_payment_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
