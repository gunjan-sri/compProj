from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupView, name='signupView'),
    path('login/', view.loginView, name='loginView'),
    path('homepage/', views.homepageView, name='homepage'),
    path('tabletennis/', views.tabletennisView, name='tabletennis' ) # URL - mySite/tabletennis
]
