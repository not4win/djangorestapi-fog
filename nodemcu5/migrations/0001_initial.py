# Generated by Django 2.0 on 2018-07-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nodemcu1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default='null', max_length=50)),
                ('temparature', models.CharField(default='null', max_length=50)),
                ('pressure', models.CharField(default='null', max_length=50)),
            ],
        ),
    ]