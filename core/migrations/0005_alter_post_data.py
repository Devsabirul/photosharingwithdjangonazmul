# Generated by Django 4.1 on 2022-08-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]