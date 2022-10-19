from django.db import models
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/")
    discription = models.TextField(max_length=200)
    data = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from="title", null=True, unique=True)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    photo = models.ImageField(upload_to="images/")
    logo = models.ImageField(upload_to="images/", null=True)
    followlink = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog_item(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", null=True, unique=True)
    description = models.TextField()
    Picture = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
