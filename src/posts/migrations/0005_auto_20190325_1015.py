# Generated by Django 2.1 on 2019-03-25 10:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190325_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 10, 15, 15, 520944, tzinfo=utc)),
        ),
    ]
