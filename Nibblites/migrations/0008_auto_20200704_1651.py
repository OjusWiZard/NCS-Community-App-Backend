# Generated by Django 3.0.8 on 2020-07-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0007_auto_20200704_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adminssion_no',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='university_roll_no',
            field=models.CharField(max_length=16),
        ),
    ]
