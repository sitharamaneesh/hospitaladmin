# Generated by Django 3.2.5 on 2021-10-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaladminapp', '0017_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='contact',
            field=models.BigIntegerField(default=0, max_length=12),
        ),
    ]
