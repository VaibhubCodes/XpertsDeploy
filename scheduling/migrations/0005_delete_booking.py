# Generated by Django 5.0 on 2024-06-19 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0004_booking_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
