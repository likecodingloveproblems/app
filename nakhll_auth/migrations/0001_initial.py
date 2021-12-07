# Generated by Django 3.1.6 on 2021-11-22 08:44

from django.db import migrations, models
import nakhll_auth.models
import nakhll_auth.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, validators=[nakhll_auth.validators.mobile_number_validator])),
                ('user_code', models.CharField(max_length=6)),
                ('auth_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('valid_to', models.DateTimeField(default=nakhll_auth.models.fivemin_from_now)),
                ('mobile_status', models.CharField(choices=[('not_reg', 'شماره موبایل ثبت نشده است'), ('login_code', 'ورود با کد'), ('login_pass', 'ورود با کلمه عبور')], max_length=10)),
                ('request_status', models.CharField(choices=[('pnd', 'در انتظار'), ('don', 'انجام شد')], default='pnd', max_length=10)),
                ('request_type', models.CharField(choices=[('signin/up', 'ورود/ثبت\u200cنام'), ('forgotpass', 'فراموشی کلمه عبور')], default='signin/up', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'درخواست احراز هویت',
                'verbose_name_plural': 'درخواست احراز هویت',
            },
        ),
    ]