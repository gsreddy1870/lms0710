# Generated by Django 5.0.1 on 2024-02-05 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0085_attendmanagecards_attendmanagecarousel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardpaymentfeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtitle', models.CharField(default=None, max_length=100)),
                ('cardcontent', models.TextField(default=None)),
                ('cardphoto', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='crpaymentfeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='paymentfeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('title1', models.CharField(default=None, max_length=100)),
                ('content1', models.TextField(default=None)),
                ('photo1', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 16, 18, 18, 157676)),
        ),
    ]
