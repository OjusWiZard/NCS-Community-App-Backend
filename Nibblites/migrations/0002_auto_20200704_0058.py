# Generated by Django 3.0.8 on 2020-07-03 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_links',
            name='behance',
        ),
        migrations.RemoveField(
            model_name='user_links',
            name='slack',
        ),
    ]
