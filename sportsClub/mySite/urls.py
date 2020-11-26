from django.urls import path
from . import views

urlpatterns = [
    path('food/',views.foodView, name='foodView'),
    path('logout/',views.logoutView, name='logoutView'),
    path('signup/', views.signupView, name='signupView'),
    path('login/', views.loginView, name='loginView'),
    path('homepage/', views.homepageView, name='homepageView'),
    path('tabletennis/', views.tabletennisView, name='tabletennis' ) # URL - mySite/tabletennis
]
