# Generated by Django 4.1 on 2022-08-24 14:27

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('about_me', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('logo', models.ImageField(null=True, upload_to='images/')),
                ('location', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('description', models.TextField()),
                ('Picture', models.ImageField(upload_to='images/')),
                ('category', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]