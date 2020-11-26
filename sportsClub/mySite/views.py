from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *


# Create your views here.

def homepageView(request):
    return render(request, 'homepage.html')

def tabletennisView(request):
    return render(request, 'tabletennis.html')

def foodView(request):
    return render(request, 'food.html')



def signupView(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html',{'error': 'Username already exists'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('mySite/homepage.html')

    else:
        return render(request, 'signup.html')

def loginView(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('mySite/homepage.html')
        else:
            return render(request, 'accounts/login.html', {'error':'the username or password is incorrect'})
    else:
        return render(request, 'login.html') 
        
def logoutView(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'mySite/signup.html')

