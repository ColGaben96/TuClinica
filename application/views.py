from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def forgot(request):
    return render(request, 'forgot.html')


def dashboard(request):
    return render(request, 'dashboard.html')
