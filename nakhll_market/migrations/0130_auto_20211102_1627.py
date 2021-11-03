# Generated by Django 3.1.6 on 2021-11-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0129_auto_20211101_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcategory',
            name='market_uuid',
            field=models.UUIDField(editable=False, null=True, verbose_name='شناسه بازار'),
        ),
        migrations.AddField(
            model_name='newcategory',
            name='submarket_uuid',
            field=models.UUIDField(editable=False, null=True, verbose_name='شناسه بازارچه'),
        ),
    ]