# Generated by Django 3.1.1 on 2020-09-24 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0002_auto_20200924_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttregister',
            old_name='tableType',
            new_name='tableNo',
        ),
    ]