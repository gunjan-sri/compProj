from django.shortcuts import render
from .models import *
import csv


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def displayRegs(request):
    return render(request, 'displayRegs.html',{
        'regs': ttRegister.objects.all()
    })

def basketball(request):
    if request.method=="POST":
        dict1=request.POST
        with open("basketball.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(request,"baskteball.html")

def badminton(request):
    if request.method=="POST":
        dict1=request.POST
        with open("badminton.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(request,"badminton.html")

def dance(request):
    if request.method=="POST":
        dict1=request.POST
        with open("dance.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(request,"baskteball.html")
