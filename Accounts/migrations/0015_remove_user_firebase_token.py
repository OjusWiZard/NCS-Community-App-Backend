# Generated by Django 3.0.8 on 2020-07-18 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_auto_20200716_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firebase_token',
        ),
    ]
