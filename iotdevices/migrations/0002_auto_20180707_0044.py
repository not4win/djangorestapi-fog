# Generated by Django 2.0 on 2018-07-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotdevices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iotdevices',
            name='value',
        ),
        migrations.AddField(
            model_name='iotdevices',
            name='pressure',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='iotdevices',
            name='temparature',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='iotdevices',
            name='device_id',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='iotdevices',
            name='time',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
