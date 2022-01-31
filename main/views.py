from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from .models import *
# Create your views here.


def index(request):

    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        user_login = request.POST['username']
        user_pass = request.POST['password']
        user = authenticate(username=user_login, password=user_pass)
        if user is not None:
            print("Правильно!")
            return redirect('index')
        else:
            print("Ой, что-то пошло не так!")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = RegisterForm(request.POST)
    context = {'form': form, }
    return render(request, 'register.html', context)
