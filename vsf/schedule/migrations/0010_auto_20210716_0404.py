# Generated by Django 3.2.5 on 2021-07-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_emailnotification_iat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailnotification',
            name='sent',
        ),
        migrations.AddField(
            model_name='emailnotification',
            name='sentat',
            field=models.DateTimeField(null=True),
        ),
    ]
