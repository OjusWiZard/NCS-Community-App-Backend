# Generated by Django 3.0.8 on 2020-07-15 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0005_auto_20200715_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='attendance_offset',
            field=models.DurationField(default=datetime.timedelta(seconds=300)),
        ),
    ]
