# Generated by Django 3.2.5 on 2021-10-02 12:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaladminapp', '0031_auto_20211002_1802'),
    ]

    operations = [
        migrations.DeleteModel(
            name='expense_in',
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='dt',
            field=models.DateField(default=datetime.datetime(2021, 10, 2, 12, 35, 12, 654777, tzinfo=utc)),
        ),
    ]