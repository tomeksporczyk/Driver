from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=64, label='Login')
    user_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Hasło')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
