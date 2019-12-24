from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {'title': 'Login Page'})


def register(request):
    return render(request, 'register.html', {'title': 'Register Page'})


def details(request):
    return render(request, 'user_details.html', {'title': 'User Details Page'})
