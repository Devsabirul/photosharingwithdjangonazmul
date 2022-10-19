from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django import forms


class HandelLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user'}))

    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password."
        )
    }


class HandelPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Current Password"),
        widget=forms.PasswordInput(
            attrs={'class': "form-control"}
        ),
    )
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(
            attrs={'class': "form-control"}
        ),
    )
    new_password2 = forms.CharField(
        label=("Confirm new password"),
        widget=forms.PasswordInput(
            attrs={'class': "form-control"}
        ),
    )

    error_messages = {
        "password_incorrect": (
            "Your old password was entered incorrectly. Please enter it again."
        ),
    }
