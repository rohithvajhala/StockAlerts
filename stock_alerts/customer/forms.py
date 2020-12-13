from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Create_user_form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "User name"}))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


