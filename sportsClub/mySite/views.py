from django.shortcuts import render
from .models import *


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def tabletennis(request):
    return render(request, 'tabletennis.html')
