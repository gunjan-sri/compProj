from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta, datetime
from django.utils import timezone
from .models import *
from .forms import *



# Create your views here.
# Homepage View
def homepageView(request):
    return render(request, 'homepage.html')


#Sports Views
def tabletennisView(request):
    tables = TTTable.objects.all()
    print(tables)
    for table in tables:
        if table.isReserved == True:
            print(table)
            try:
                curRes = TTReservation.objects.filter(tableName=table).first()
                print(curRes)
                curTime = curRes.resTime
                curDate = curRes.resDate
                delta = timedelta(hours=1)
                addedTime = (datetime.combine(curDate, curTime)+delta)

                if (timezone.now().date() >= curDate) and (timezone.now().time() >= addedTime.time()):
                    table.isReserved = False
                    table.save()
                    curRes.delete()
            except ObjectDoesNotExist:
                pass

    form=tabletennisForm(request.user, request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        tableNameValue = form.cleaned_data.get('tablename')
        resTimeValue = form.cleaned_data.get('restime')
        resDateValue=form.cleaned_data.get('resdate')
        tables = TTTable.objects.filter(tblType=tableNameValue)
        for table in tables:
            if table.isReserved == False:
                table.isReserved = True
                table.save()
                # Creating the reservation
                curUser = User.objects.get(username=f'{request.user}')
                curRes = TTReservation(customer=curUser, tableName=table, resTime=f'{resTimeValue}', resDate=f'{resDateValue}')
                curRes.save()
                context = {'form': form, 'message': 'Reservation Successful!'}
                return render(request, 'tabletennis.html', context)
    else:
        context = {'form': form}
        return render(request, 'tabletennis.html', context)

def badmintonView(request):
    courts = BTCourt.objects.all()
    print(courts)
    for court in courts:
        if court.isReserved == True:
            print(court)
            try:
                curRes = BTReservation.objects.filter(BTCourtName=court).first()
                print('in try', curRes)
                if curRes is not None:
                    print(curRes, 'is not none')
                    curTime = curRes.BTresTime
                    print(curTime)
                    curDate = curRes.BTresDate
                    print(curDate)
                    delta = timedelta(hours=1)
                    addedTime = (datetime.combine(curDate, curTime)+delta)

                    if (timezone.now().date() >= curDate) and (timezone.now().time() >= addedTime.time()):
                        court.isReserved = False
                        court.save()
                        curRes.delete()
                else:
                    pass
            except ObjectDoesNotExist:
                pass

    form=badmintonForm(request.user, request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        courtNameValue = form.cleaned_data.get('btcourtname')
        resTimeValue = form.cleaned_data.get('btrestime')
        print(f'restimevalue {resTimeValue}')
        resDateValue=form.cleaned_data.get('btresdate')
        print(f'resdimevalue {resDateValue}')
        courts = BTCourt.objects.filter(BTcourtLocation=courtNameValue)
        for court in courts:
            print('entered')
            if court.isReserved == False:
                court.isReserved = True
                court.save()
                print('saved court reserve')
                # Creating the reservation
                print('creating reservation:')
                curUser = User.objects.get(username=f'{request.user}')
                curRes = BTReservation(customer=curUser, BTCourtName=court, BTresTime=f'{resTimeValue}', BTresDate=f'{resDateValue}')
                print(f'Curres {curRes}')
                curRes.save()
                context = {'form': form, 'message': 'Reservation Successful!'}
                return render(request, 'badminton.html', context)
    else:
        context = {'form': form}
        return render(request, 'badminton.html', context)

def squashView(request):
    courts = SCourt.objects.all()
    for court in courts:
        if court.isReserved == True:
            try:
                curRes = SReservation.objects.filter(SCourtName=court).first()
                if curRes is not None:
                    curTime = curRes.SresTime
                    curDate = curRes.SresDate
                    delta = timedelta(hours=1)
                    addedTime = (datetime.combine(curDate, curTime)+delta)

                    if (timezone.now().date() >= curDate) and (timezone.now().time() >= addedTime.time()):
                        court.isReserved = False
                        court.save()
                        curRes.delete()
                else:
                    pass
            except ObjectDoesNotExist:
                pass

    form=squashForm(request.user, request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        courtNameValue = form.cleaned_data.get('scourtname')
        resTimeValue = form.cleaned_data.get('srestime')
        resDateValue=form.cleaned_data.get('sresdate')
        courts = SCourt.objects.all()
        for court in courts:
            if court.isReserved == False:
                court.isReserved = True
                court.save()
                # Creating the reservation
                curUser = User.objects.get(username=f'{request.user}')
                curRes = SReservation(customer=curUser, SCourtName=court, SresTime=f'{resTimeValue}', SresDate=f'{resDateValue}')
                curRes.save()
                context = {'form': form, 'message': 'Reservation Successful!'}
                return render(request, 'squash.html', context)
    else:
        context = {'form': form}
        return render(request, 'squash.html', context)

def tennisView(request):
    courts = TCourt.objects.all()
    for court in courts:
        if court.isReserved == True:
            try:
                curRes = TReservation.objects.filter(TCourtName=court).first()
                if curRes is not None:
                    curTime = curRes.TresTime
                    curDate = curRes.TresDate
                    delta = timedelta(hours=1)
                    addedTime = (datetime.combine(curDate, curTime)+delta)

                    if (timezone.now().date() >= curDate) and (timezone.now().time() >= addedTime.time()):
                        court.isReserved = False
                        court.save()
                        curRes.delete()
                else:
                    pass
            except ObjectDoesNotExist:
                pass

    form=tennisForm(request.user, request.POST)
    if form.is_valid():
        fs=form.save(commit=False)
        courtNameValue = form.cleaned_data.get('tcourtname')
        resTimeValue = form.cleaned_data.get('trestime')
        resDateValue=form.cleaned_data.get('tresdate')
        courts = TCourt.objects.filter(TcourtLocation=courtNameValue)
        for court in courts:
            if court.isReserved == False:
                court.isReserved = True
                court.save()
                # Creating the reservation
                curUser = User.objects.get(username=f'{request.user}')
                curRes = TReservation(customer=curUser, TCourtName=court, TresTime=f'{resTimeValue}', TresDate=f'{resDateValue}')
                curRes.save()
                context = {'form': form, 'message': 'Reservation Successful!'}
                return render(request, 'tennis.html', context)
    else:
        context = {'form': form}
        return render(request, 'tennis.html', context)

def gymView(request):
    return render(request, 'gym.html')

#Extras Views
def feesView(request):
    return render(request, 'fees.html')

def logged(request):
    return render(request, 'thank.html')

#Signup, Login and Logout Views
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
        firstname=form.cleaned_data.get('firstname')
        lastname=form.cleaned_data.get('lastname')
        emailvalue=form.cleaned_data.get('email')
        uservalue=form.cleaned_data.get('username')
        password1value=form.cleaned_data.get('password1')
        password2value=form.cleaned_data.get('password2')
        if password1value==password2value:
            try:
                user=User.objects.get(username=uservalue)
                context={'form':form, 'error':'The username you entered has already been taken'}
                return render(request, 'signup.html', context)
            except User.DoesNotExist:
                user=User.objects.create_user(uservalue,password= password1value,email=emailvalue, first_name=firstname, last_name=lastname)
                user.save()
                login(request,user)
                fs.user= request.user
                fs.save()
                context = {'form': form, 'error': 'Sign Up Successful!'}
                return render(request, 'signup.html', context)
        else:
            context={'form':form,'error':'The passwords that you provided do not match'}
            return render(request, 'signup.html',context)
    else:
        context={'form':form}
        return render(request, 'signup.html',context)

def loginView(request):
    uservalue=''
    passwordvalue=''
    form=loginForm(request.POST)
    if form.is_valid():
        uservalue=form.cleaned_data.get('username')
        passwordvalue=form.cleaned_data.get('password')

        user=authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            auth.login(request,user)
            context= {'form': form, 'error': 'The login has been successful'}
            return render(request, 'homepage.html', context)
        else:
            context={'form':form, 'error':'The username and password combination is incorrect'}
            return render(request, 'login.html', context)
    else:
        context={'form':form}
        return render(request, 'login.html', context)

def logoutView(request):
    if request.method=='POST':
        logout(request)
    return render(request, 'homepage.html')
