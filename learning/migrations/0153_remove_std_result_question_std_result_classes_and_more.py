# Generated by Django 5.0.1 on 2024-03-12 09:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0152_remove_quiz_questions_order_alter_leave_today_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='std_result',
            name='question',
        ),
        migrations.AddField(
            model_name='std_result',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.cls_name'),
        ),
        migrations.AddField(
            model_name='std_result',
            name='questionstd',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='std_result',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.student'),
        ),
        migrations.AddField(
            model_name='std_result',
            name='subject_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.subject'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 9, 24, 6, 190147)),
        ),
        migrations.AlterField(
            model_name='std_result',
            name='answer',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 12, 9, 24, 6, 173148)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 12, 9, 24, 6, 173148)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 12, 9, 24, 6, 173148)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 12, 9, 24, 6, 173148)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 3, 12, 9, 24, 6, 173148)),
        ),
    ]
