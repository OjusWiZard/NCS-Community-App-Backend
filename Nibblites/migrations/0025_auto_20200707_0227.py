# Generated by Django 3.0.8 on 2020-07-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nibblites', '0024_auto_20200707_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]