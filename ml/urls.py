from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('choose',views.choose,name="choose"),
    path('heart',views.heart,name="heart"),
    path('after',views.after,name="after"),
    path('register',views.register,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('after2',views.after2,name="after2"),
    path('liver',views.liver,name="liver"),
    path('after3',views.after3,name="after3"),
    path('chronic',views.chronic,name="chronic"),
    path('services',views.services,name="services"),
]