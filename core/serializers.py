from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class BlogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_item
        fields = "__all__"
