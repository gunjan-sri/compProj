# Generated by Django 3.1.1 on 2020-11-29 05:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=25)),
                ('password1', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('birth_date', models.DateField(verbose_name='YYYY-M-DD')),
                ('email', models.EmailField(max_length=15)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='TTTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tblLocation', models.CharField(choices=[('1', 'Floor 1'), ('2', 'Floor 2')], default='1', max_length=2)),
                ('tblType', models.CharField(choices=[('kids', 'Kids Table'), ('adult', 'Adult Table')], default='adult', max_length=5)),
                ('isReserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TTReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resDate', models.DateField(default=datetime.date(2020, 11, 29))),
                ('resTime', models.TimeField(default=datetime.time(5, 1, 19, 230500))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='mySite.member')),
                ('tableName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='mySite.tttable')),
            ],
        ),
    ]
