from django.urls import path
from .views import *
urlpatterns = [
    path('', login, name="login"),
    path('logout', user_logout, name="user_logout"),
]
