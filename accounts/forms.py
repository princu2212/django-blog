from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name')