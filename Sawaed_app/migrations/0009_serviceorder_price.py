# Generated by Django 5.1.6 on 2025-04-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sawaed_app', '0008_serviceorder_handyman_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
