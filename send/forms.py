from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForms(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))