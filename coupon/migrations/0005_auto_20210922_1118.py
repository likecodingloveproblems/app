# Generated by Django 3.1.6 on 2021-09-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0004_auto_20210901_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='max_amount',
            field=models.IntegerField(default=0, verbose_name='حداکثر تخفیف قابل اعمال'),
        ),
    ]