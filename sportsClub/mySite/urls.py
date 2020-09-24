from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('displayRegs/', views.displayRegs, name='displayRegs')
]
