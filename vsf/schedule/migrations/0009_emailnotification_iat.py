# Generated by Django 3.2.5 on 2021-07-16 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_emailnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='iat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
