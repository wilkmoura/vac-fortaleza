# Generated by Django 3.2.5 on 2021-07-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210707_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadsheet',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
