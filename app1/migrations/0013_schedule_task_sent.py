# Generated by Django 4.0.4 on 2022-04-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_schedule_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule_task',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
