from django.shortcuts import render
from .models import *


# Create your views here.

def homepageView(request):
    return render(request, 'homepage.html')

def tabletennisView(request):
    return render(request, 'tabletennis.html')
