# Generated by Django 2.2.5 on 2021-06-08 00:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210608_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 0, 9, 35, 998872, tzinfo=utc)),
        ),
    ]
