from django.urls import path
from . import views

urlpatterns=[
    path('PPFaction/',views.PPFaction,name='PPFaction'),
    path('APYaction/',views.APYaction,name='APYaction'),
    path('PMVYYaction/',views.PMVYYaction,name='PMVYYaction'),
    path('SSYaction/',views.SSYaction,name='SSYaction'),
    path('loanpage/',views.loanpage,name='loanpage'),
    path('homeloanaction/',views.homeloanaction,name='homeloanaction'),
    path('eduloanaction/',views.eduloanaction,name='eduloanaction'),
    path('back2/',views.back2,name='back2'),
    path('home2/',views.home2,name='home2'),
    path('welcome/',views.welcome,name='welcome'),
    path('welcome2/',views.welcome2,name='welcome2'),
    path('back/',views.back,name='back')
]