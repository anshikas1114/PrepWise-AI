from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('profile')

    return render(request, 'accounts/register.html')