# Generated by Django 2.1.7 on 2019-04-30 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0012_auto_20190501_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='7F79D5289D42', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADDA934F6D1F', max_length=14),
        ),
    ]
