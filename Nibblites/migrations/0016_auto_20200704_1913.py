# Generated by Django 3.0.8 on 2020-07-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0015_auto_20200704_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_links',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_links',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
    ]