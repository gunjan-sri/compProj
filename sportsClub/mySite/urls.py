from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepageView, name='homepage'),
    path('tabletennis/', views.tabletennisView, name='tabletennis' ) # URL - mySite/tabletennis
]
