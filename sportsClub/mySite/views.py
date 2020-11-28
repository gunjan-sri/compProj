from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *


# Create your views here.
# Homepage View
def homepageView(request):
    return render(request, 'homepage.html')


    #Sports Views 

def tabletennisView(request):
    tables = TTTable.objects.all()

    for table in tables:
        print(table)
        if table.isReserved == True:

            curRes = TTReservation.objects.get(tableName=table)
            print(f'Current reservaton: {curRes}')

            curTime = curRes.resTime # resTime = timezone.now().time()
            curDate = curRes.resDate
            delta = timedelta(hours=1)
            addedTime = (datetime.combine(curDate, curTime)+delta).time()

            if timezone.now().time() > addedTime:

                print(f'Table saved is {table.isReserved}')
                table.isReserved = False
                table.save()
                print(f'Table saved is {table.isReserved}')

                curRes.delete()

    if request.method == 'POST':
        firstn = request.POST['customer-first']
        lastn = request.POST['customer-last']
        customer = ClubMember.objects.get(firstname=firstn, lastname=lastn)

        tables = TTTable.objects.all()

        for table in tables:
            if table.isReserved == True:
                pass
            else:
                #tblLoc = table.tblLocation
                table.isReserved = True
                table.save()
                ttype = request.POST['table-type']
                tblTime = request.POST['table-timings']
                reservation = TTReservation.objects.create(customer=customer, tableName=table, resTime=tblTime)
                reservation.save()
                break

    return render(request, 'index.html', {
        'members':ClubMember.objects.all(),
        'reservations':TTReservation.objects.all()
    })

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
def faqView(request):
    return render(request, 'faq.html')

def feesView(request):
    return render(request, 'fees.html')



#Signup, Login and Logout Views

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
