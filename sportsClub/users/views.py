from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
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
        
def logout(request):
    if request.method=='POST'
    auth.logout(request)
    return render(request, 'mySite/homepage.html')

