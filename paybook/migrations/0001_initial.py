# Generated by Django 5.1.1 on 2024-11-11 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0037_alter_booking_wallet_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommissionSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_type', models.CharField(choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')], default='percentage', max_length=10)),
                ('value', models.DecimalField(decimal_places=2, help_text='Percentage or fixed amount based on type', max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='PaybookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission_deducted', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credited_to_wallet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paybook_entry', to='core.booking')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paybook_entries', to='core.mentor')),
            ],
        ),
    ]
