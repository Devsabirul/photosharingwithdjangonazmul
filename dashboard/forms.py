from django import forms
from core.models import *


class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mt-3'}),
            "discription": forms.Textarea(attrs={'class': 'form-control mt-3'}),
            'picture': forms.FileInput(attrs={'class': 'form-control mt-3 remove_t', 'title': 'Replase Picture'}),
        }


class About_form(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control mt-3'}),
            "about_me": forms.Textarea(attrs={'class': 'form-control mt-3'}),
            'photo': forms.FileInput(attrs={'class': 'form-control mt-3'}),
            'logo': forms.FileInput(attrs={'class': 'form-control mt-3'}),
            "followlink": forms.TextInput(attrs={'class': 'form-control mt-3'}),
        }


class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog_item
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog title'}),
            "description": forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog description'}),
            "category": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog Category '}),
            "author": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog Author '}),
            'Picture': forms.FileInput(attrs={'class': 'form-control mt-3'}),
        }
