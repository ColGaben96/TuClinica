from django.shortcuts import render


def login(request):
    return render(request, 'login-ad.html')


def dashboard(request):
    return render(request, 'dashboard-ad.html')
