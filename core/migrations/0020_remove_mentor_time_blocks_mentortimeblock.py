# Generated by Django 5.0 on 2024-08-30 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_customuser_otp_otp'),
        
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='time_blocks',
        ),
        migrations.CreateModel(
            name='MentorTimeBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_time_blocks', to='core.mentor')),
                ('time_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_time_blocks', to='time_blocks.timeblock')),
            ],
            options={
                'unique_together': {('mentor', 'time_block')},
            },
        ),
    ]
