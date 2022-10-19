from django.shortcuts import render
from .models import About, Post
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
# Create your views here.


def home(request):
    post = Post.objects.order_by("-id")
    about = About.objects.all()
    context = {
        'content': post,
        'about': about
    }
    return render(request, 'home/index.html', context)


def single_post(request, slug):
    post = Post.objects.get(slug=slug)
    about = About.objects.all()
    return render(request, 'singlepage/single_post.html', {'content': post, 'about': about})


# Api Created Start
class PostApiView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            post = Post.objects.get(pk=id)
            serializers = PostSerializer(post)
            return Response({'status': 'success', "post": serializers.data}, status=status.HTTP_200_OK)
        post = Post.objects.all()
        serializers = PostSerializer(post, many=True)
        return Response({'status': 'success', "post": serializers.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', "post": serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'errors', 'post': serializers.errors})

    def put(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(pk=id)
        serializers = PostSerializer(post, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializers.errors)

    def patch(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(pk=id)
        serializers = PostSerializer(post, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializers.errors)

    def delete(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(pk=id)
        post.delete()

        return Response({'message': 'Data Deleted successfully'})


class AboutApiView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            about = About.objects.get(pk=id)
            serializers = AboutSerializer(about)
            return Response({'status': 'success', "About": serializers.data}, status=status.HTTP_200_OK)
        about = About.objects.all()
        serializers = AboutSerializer(about, many=True)
        return Response({'status': 'success', "About": serializers.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = AboutSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', "About": serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'errors', 'About': serializers.errors})

    def patch(self, request, pk, format=None):
        id = pk
        about = About.objects.get(pk=id)
        serializers = AboutSerializer(about, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializers.errors)
