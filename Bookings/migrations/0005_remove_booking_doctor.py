# Generated by Django 5.1.5 on 2025-01-22 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0004_alter_booking_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='doctor',
        ),
    ]
