from django.shortcuts import render
import csv

# Create your views here.
def basketball(reuqest):
    if request.method=="POST":
        dict1=request.POST
        with open("basketball.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(reuqest,"baskteball.html")

def badminton(request):
    if request.method=="POST":
        dict1=request.POST
        with open("badminton.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(reuqest,"badminton.html")

def dance(request):
    if request.method=="POST":
        dict1=request.POST
        with open("dance.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key,value])

    return render(reuqest,"baskteball.html")


