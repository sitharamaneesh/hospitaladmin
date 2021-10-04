# Generated by Django 3.2.5 on 2021-10-01 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaladminapp', '0029_auto_20211001_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='medname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='pres',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='dt',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 17, 51, 31, 122422, tzinfo=utc)),
        ),
    ]