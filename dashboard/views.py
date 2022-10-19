from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .forms import *
from core.models import Post, About
from .forms import *
from login.forms import *
from django.contrib.auth.models import User


def dashboard(request):
    return redirect('/dashboard/profile')


def create_post(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        if request.method == 'POST':
            data = request.POST
            title = data.get('title')
            picture = request.FILES['profile_pic']
            discription = data.get('discription')
            post = Post(title=title, picture=picture, discription=discription)
            post.save()
        return render(request, 'dashboard/create_post.html', {'about': about})
    else:
        return redirect('/NH-admin')


def update_post(request, id):
    if request.user.is_authenticated:
        about = About.objects.all()
        if request.method == "POST":
            get_id = Post.objects.get(id=id)
            fm = Post_form(request.POST, request.FILES, instance=get_id)
            if fm.is_valid():
                fm.save()
                return redirect("profile")
        else:
            get_id = Post.objects.get(id=id)
            fm = Post_form(instance=get_id)
        return render(request, 'dashboard/update_post.html', {'about': about, 'form': fm})
    else:
        return redirect('/NH-admin')


def profile(request):
    if request.user.is_authenticated:
        post = Post.objects.order_by("-id")
        about = About.objects.all()
        user = User.objects.all()
        user_lenght = len(user)
        l = len(post)
        length_ = len(about)
        if length_ == 0:
            return redirect('/dashboard/add-profile')
        else:
            context = {
                'content': post,
                'length': l,
                'about': about,
                'user_lenght': user_lenght,
            }
            return render(request, 'dashboard/profile.html', context)
    else:
        return redirect('/NH-admin')


def add_profile(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        length_ = len(about)
        if length_ == 0:
            if request.method == "POST":
                form = About_form(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            else:
                form = About_form()
            return render(request, 'dashboard/add_profile.html', {'about': about, 'form': form})
        else:
            return redirect('/dashboard')
    else:
        return redirect('/NH-admin')


def upload_profile(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        if request.method == "POST":
            get_id = About.objects.get(id=1)
            form = About_form(request.POST, request.FILES, instance=get_id)
            if form.is_valid():
                form.save()
        else:
            get_id = About.objects.get(id=1)
            form = About_form(instance=get_id)
        return render(request, 'dashboard/upload_profile.html', {'about': about, 'form': form})
    else:
        return redirect('/NH-admin')


def change_password(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        if request.method == "POST":
            fm = HandelPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('/dashboard')
        else:
            fm = HandelPasswordForm(user=request.user)
        return render(request, 'dashboard/change_password.html', {'form': fm, 'about': about})
    else:
        return redirect("/NH-admin")


def delete(request):
    data = request.POST
    id = data.get('id')
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("profile")
