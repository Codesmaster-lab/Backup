from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.shortcuts import render,redirect

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=100, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model =User
        fields=('username','email','password1','password2','first_name','last_name')


class UserUpdateForm(forms.ModelForm):
    email:forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserUpdateForm2(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('image','description')
