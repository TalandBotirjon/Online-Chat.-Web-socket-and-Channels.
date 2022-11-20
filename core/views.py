from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{username} you login Online chat site.")
            return redirect('/')
        else:
            messages.error(request, f'Not user login. Please check username or password.')
    return render(request, 'core/login.html')
