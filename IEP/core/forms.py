from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email"]


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput}
