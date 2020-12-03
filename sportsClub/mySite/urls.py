from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageView, name='homepageView'),
    path('tabletennis/', views.tabletennisView, name='tabletennisView' ),
    path('badminton/', views.badmintonView, name='badmintonView'),
    path('squash/', views.squashView, name='squashView'),
    path('tennis/', views.tennisView, name='tennisView'),
    path('gym/', views.gymView, name='gymView'),
    path('fees/', views.feesView, name='feesView'),
    path('logout/',views.logoutView, name='logoutView'),
    path('thankyou/',views.logged, name='thankyou'),
    path('signup/', views.signupView, name='signupView'),
    path('login/', views.loginView, name='loginView'),

]
