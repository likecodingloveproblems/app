# Generated by Django 3.2.14 on 2022-08-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20220209_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='paid_by_coin',
            field=models.BooleanField(
                default=False,
                verbose_name='پرداخت سکه دارد؟'),
        ),
    ]