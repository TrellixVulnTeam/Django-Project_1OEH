# Generated by Django 2.2.4 on 2019-09-28 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190926_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_participants',
            name='userName',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
