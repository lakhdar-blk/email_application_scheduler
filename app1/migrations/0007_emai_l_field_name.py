# Generated by Django 4.0.4 on 2022-04-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_emai_l_r_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='emai_l',
            name='field_name',
            field=models.DateTimeField(null=True),
        ),
    ]