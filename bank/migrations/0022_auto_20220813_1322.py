# Generated by Django 3.2.14 on 2022-08-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0021_alter_accountrequest_request_type'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='accountrequest',
            name='staff_user_check_for_different_statuses',
        ),
        migrations.AlterField(
            model_name='coinmintburn',
            name='is_mint',
            field=models.BooleanField(default=True, verbose_name='آیا ضرب سکه است؟'),
        ),
        migrations.AddConstraint(
            model_name='accountrequest',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('status__in', [1, 2]), models.Q(('staff_user', None), _negated=True)), models.Q(('staff_user', None), models.Q(('status', 0), ('request_type__in', [0, 1, 2, 3]), _connector='OR')), _connector='OR'), name='staff_user_check_for_different_statuses'),
        ),
    ]