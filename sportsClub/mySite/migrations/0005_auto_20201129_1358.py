# Generated by Django 3.1 on 2020-11-29 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0004_auto_20201129_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttreservation',
            name='resTime',
            field=models.TimeField(default=datetime.time(4, 58, 45, 874791)),
        ),
    ]
