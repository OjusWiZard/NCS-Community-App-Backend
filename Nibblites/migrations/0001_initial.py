# Generated by Django 3.0.8 on 2020-07-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_tech', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_tech', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontend_tech', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_tech_stack', models.ManyToManyField(blank=True, null=True, to='Nibblites.AppTech')),
                ('backend_stack', models.ManyToManyField(blank=True, null=True, to='Nibblites.Backend')),
                ('frontend_stack', models.ManyToManyField(blank=True, null=True, to='Nibblites.Frontend')),
                ('languages', models.ManyToManyField(blank=True, null=True, to='Nibblites.Language')),
            ],
        ),
    ]
