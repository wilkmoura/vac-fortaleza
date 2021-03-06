# Generated by Django 3.2.5 on 2021-07-07 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_schedule_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='iat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='spreadsheet_line',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='spreadsheet_page',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spreadsheet',
            name='iat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spreadsheet',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
