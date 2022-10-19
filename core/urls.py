from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="Home"),
    path('pin/<slug:slug>', single_post, name="single_post"),
    path('api/post', PostApiView.as_view(), name="PostApiView"),
    path('api/post/<int:pk>/', PostApiView.as_view(), name="PostApiView"),
    path('api/about', AboutApiView.as_view(), name="AboutApiView"),
    path('api/about/<int:pk>/', AboutApiView.as_view(), name="AboutApiView"),
]
