from django.urls import path
from .views import *
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('profile', profile, name="profile"),
    path('upload-profile', upload_profile, name="upload_profile"),
    path('add-profile', add_profile, name="add_profile"),
    path('change-password', change_password, name="change_password"),
    path('create-post', create_post, name="create_post"),
    path('update-post/<int:id>', update_post, name="update_post"),
    path('delete-post', delete, name="delete"),
]
