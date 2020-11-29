from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *



# Create your views here.
# Homepage View
def homepageView(request):
    return render(request, 'homepage.html')


    #Sports Views

def tabletennisView(request):
    form=tabletennisForm(request.user, request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        # user = user.get
        tableNameValue = form.cleaned_data.get('tablename')
        resTimeValue=form.cleaned_data.get('restime')
        resDateValue=form.cleaned_data.get('resdate')


        tables = TTTable.objects.filter(tblType=tableNameValue)
        for table in tables:
            if table.isReserved == False:
                table.isReserved = True
                table.save()
                savedTable=table
                break

        # Creating the reservation
        curRes = TTReservation.create(customer=user, tableName=savedTable, resDate=resDateValue, resTime=resTimeValue)
        curRes.save()
        print('Saved Reservation')
        print(f'{TTReservation.objects.all()}')
        context = {'form': form, 'message': 'Reservation Successful!'}
        return render(request, 'tabletennis.html', context)
    else:
        context = {'form': form}
        return render(request, 'tabletennis.html', context)

    return render(request, 'tabletennis.html')

def badmintonView(request):
    return render(request, 'badminton.html')

def squashView(request):
    return render(request, 'squash.html')

def tennisView(request):
    return render(request, 'tennis.html')

def gymView(request):
    return render(request, 'gym.html')

  #Extras Views

def feesView(request):
    return render(request, 'fees.html')



#Signup, Login and Logout Views

"""def signupView(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        DOB=request.POST['DOB']
        password=request.POST['password1']
        try:
            user=User.objects.get(username=request.POST['username'])
            return render(request, 'signup.html',{'error': 'Username already exists'})
        except User.DoesNotExist:
            user=User.objects.create_user(DOB, firstname, address, email, lastname,password,request.POST['username'])
            auth.login(request,user)
            return redirect('homepage.html')

    else:
        return render(request, 'signup.html')"""



def signupView(request):
    firstname=''
    lastname=''
    emailvalue=''
    uservalue=''
    password1value=''
    password2value=''

    form=signupForm(request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        firstname=form.cleaned_data.get('first_name')
        lastname=form.cleaned_data.get('last_name')
        emailvalue=form.cleaned_data.get('email')
        uservalue=form.cleaned_data.get('username')
        password1value=form.cleaned_data.get('password1')
        password2value=form.cleaned_data.get('password2')
        if password1value==password2value:
            try:
                user=User.objects.get(username=uservalue)
                context={'form':form, 'error':'The username you entered has already been taken'}
                return render(request, 'signup.html')
            except User.DoesNotExist:
                user=User.objects.create_user(uservalue,password= password1value,email=emailvalue)
                user.save()


                login(request,user)

                fs.user= request.user

                fs.save()
                context= {'form': form}
                return render(request, 'signup.html', context)

        else:
            context={'form':form,'error':'The passwords that you provided do not match'}
            return render(request, 'signup.html',context)

    else:
        context={'form':form}
        return render(request, 'signup.html',context)


"""def loginView(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('homepage.html')
        else:
            return render(request, 'login.html', {'error':'the username or password is incorrect'})
    else:
        return render(request, 'login.html')"""

def loginView(request):
    uservalue=''
    passwordvalue=''
    form=loginForm(request.POST)
    if form.is_valid():
        uservalue=form.cleaned_data.get('username')
        passwordvalue=form.cleaned_data.get('password')

        user=authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request,user)
            context= {'form': form, 'error': 'The login has been successful'}
            return render(request, 'login.html', context)
        else:
            context={'form':form, 'error':'The username and password combination is incorrect'}
            return render(request, 'login.html', context)
    else:
        context={'form':form}
        return render(request, 'login.html', context)
        
def logoutView(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('homepage.html')
    
    return render(request, 'thank.html')

def logged(request):
    return render(request, 'thank.html')

