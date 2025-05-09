# Generated by Django 5.1.7 on 2025-04-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sawaed_app', '0009_serviceorder_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicelisting',
            name='service_type',
            field=models.CharField(blank=True, choices=[('السباكة', 'السباكة'), ('النجارة', 'النجارة'), ('الطبخ', 'الطبخ'), ('التصوير', 'التصوير'), ('الكهرباء', 'الكهرباء'), ('التكييف والتبريد', 'التكييف والتبريد'), ('التنظيف', 'التنظيف'), ('الميكانيكا', 'الميكانيكا'), ('الدهان', 'الدهان'), ('الحدادة', 'الحدادة'), ('التمديدات الصحية', 'التمديدات الصحية'), ('البرمجة وتطوير المواقع', 'البرمجة وتطوير المواقع'), ('التصميم الجرافيكي', 'التصميم الجرافيكي'), ('الترجمة', 'الترجمة'), ('الكتابة والتحرير', 'الكتابة والتحرير'), ('خدمات أخرى', 'خدمات أخرى')], default='خدمات أخرى', max_length=50, null=True),
        ),
    ]
