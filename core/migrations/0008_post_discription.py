# Generated by Django 4.1 on 2022-08-26 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='discription',
            field=models.TextField(default=datetime.datetime(2022, 8, 26, 15, 54, 35, 144628, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]
