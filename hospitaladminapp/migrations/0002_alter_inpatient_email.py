# Generated by Django 3.2.5 on 2021-09-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaladminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inpatient',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
