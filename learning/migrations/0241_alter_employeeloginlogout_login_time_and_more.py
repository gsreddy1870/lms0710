# Generated by Django 4.1.3 on 2024-07-25 04:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0240_alter_employeeloginlogout_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 25, 10, 0, 10, 602750)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 25, 10, 0, 10, 631682)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 7, 25, 10, 0, 10, 599758)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 7, 25, 10, 0, 10, 599758)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 7, 25, 10, 0, 10, 608735)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 7, 25, 10, 0, 10, 608735)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 7, 25, 10, 0, 10, 608735)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 7, 25, 10, 0, 10, 608735)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 10, 0, 10, 607739)),
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.student')),
            ],
        ),
    ]
