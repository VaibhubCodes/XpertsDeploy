# Generated by Django 5.1.1 on 2024-10-06 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_expertise_group_post_group'),
        ('industry', '0002_expertise_expertise_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='mentee',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('poll', 'Poll'), ('document', 'Document'), ('pdf', 'PDF'), ('link', 'Link')], default='text', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='expertise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='industry.expertise'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='community.group'),
        ),
        migrations.CreateModel(
            name='SubscriptionPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=255, unique=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='community.subscription')),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='community.subscriptionplan'),
        ),
    ]
