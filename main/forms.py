from django.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
        widgets = {
            "email": EmailInput(attrs={'class': '', 'placeholder': 'Введите электронную почту'}),
            "password1": PasswordInput(attrs={'class': '', 'placeholder': 'Введите пароль'}),
            "password2": PasswordInput(attrs={'class': '', 'placeholder': 'Подтвердите пароль'}),
        }
