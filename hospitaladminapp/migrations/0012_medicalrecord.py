# Generated by Django 3.2.5 on 2021-09-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaladminapp', '0011_alter_inpatient_medical_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('records', models.CharField(max_length=200)),
            ],
        ),
    ]
