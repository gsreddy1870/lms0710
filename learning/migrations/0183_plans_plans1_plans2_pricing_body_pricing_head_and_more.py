# Generated by Django 4.2.4 on 2024-04-10 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0182_hero_alter_leave_today_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=100)),
                ('amt', models.IntegerField()),
                ('features', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='plans1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan1', models.CharField(max_length=100)),
                ('amt1', models.IntegerField()),
                ('features1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='plans2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan2', models.CharField(max_length=100)),
                ('amt2', models.IntegerField()),
                ('features2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pricing_body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('icon', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pricing_head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 10, 14, 39, 20, 199236)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 10, 14, 39, 20, 175181)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 10, 14, 39, 20, 175181)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 10, 14, 39, 20, 175181)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 10, 14, 39, 20, 175181)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 4, 10, 14, 39, 20, 175181)),
        ),
    ]
