# Generated by Django 4.0.4 on 2022-04-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_rename_field_name_emai_l_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='emai_l',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
