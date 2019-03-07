from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.views import *

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
        else:
            return render(request, 'login.html', {'errors': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password1'],
            first_name=request.POST['First_name'],
            last_name=request.POST['Last_name']
            )
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
    return render(request, 'signup.html')

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
logout = LogoutViews.as_view()
# def logout(request):
#     if request.method == "POST":
#         auth.logout(request)
#         return redirect('logout')
#     return render(request, 'home.html')
