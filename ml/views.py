from django.shortcuts import render,redirect
from flask import request_finished
from .models import forms,forms3,forms2
import pickle
import numpy as np
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,"home.html")

def choose(request):
    return render(request,"choose.html")

def heart(request):
    return render(request,"disease.html")
def liver(request):
    return render(request,"liver.html")
def chronic(request):
    return render(request,'chronic.html')

def after(request):
    model = pickle.load(open('iri.pkl', 'rb'))
    if request.method == "POST":
        data1=request.POST['a']
        data2=request.POST['b']
        data3=request.POST['c']
        data4=request.POST['d']
        data5=request.POST['e']
        data6=request.POST['f']
        data7=request.POST['g']
        data8=request.POST['h']
        data9=request.POST['i']
        data10=request.POST['j']
        data11=request.POST['k']
        data12=request.POST['l']
        data13=request.POST['m']
        data14=request.POST['n']    
        data15=request.POST['username']
        data16=request.POST['city']
        category='Heart'
        # data17=request.POST['date']

    # return render(request,"after.html")
        arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14]],dtype=int)
        pred = model.predict(arr)

        after=forms(a=data1,b=data2,c=data3,d=data4,e=data5,f=data6,g=data7,h=data8,i=data9,j=data10,k=data11,l=data12,m=data13,n=data14,username=data15,city=data16,pred=pred,category=category)
        after.save()
    return render(request,'after.html', {'data':pred})

def after2(request):
    model = pickle.load(open('liver.pkl', 'rb'))
    if request.method == "POST":
        data1=request.POST['a']
        data2=request.POST['b']
        data3=request.POST['c']
        data4=request.POST['d']
        data5=request.POST['e']
        data6=request.POST['f']
        data7=request.POST['g']
        data8=request.POST['h']
        data9=request.POST['i']
        data10=request.POST['j']
        data15=request.POST['username']
        data16=request.POST['city']
        category='Liver'
        

    # return render(request,"after.html")
        arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10]],dtype=int)
        pred = model.predict(arr)

        after2=forms2(a=data1,b=data2,c=data3,d=data4,e=data5,f=data6,g=data7,h=data8,i=data9,j=data10,username=data15,city=data16,pred=pred,category=category)
        after2.save()
    return render(request,'after2.html', {'data':pred})


def after3(request):
    model = pickle.load(open('chronic.pkl', 'rb'))
    if request.method == "POST":
        data1=request.POST['a']
        data2=request.POST['b']
        data3=request.POST['c']
        data4=request.POST['d']
        data5=request.POST['e']
        data6=request.POST['f']
        data7=request.POST['g']
        data8=request.POST['h']
        data9=request.POST['i']
        data10=request.POST['j']
        data11=request.POST['k']
        data12=request.POST['l']
        data13=request.POST['m']
        data14=request.POST['n']
        data15=request.POST['o']
        data16=request.POST['p']
        data17=request.POST['q']
        data18=request.POST['username']
        data19=request.POST['city']
        category='Chronic'
        data20=request.POST['c']
        

    # return render(request,"after.html")
        arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data20]],dtype=int)
        pred = model.predict(arr)

        after3=forms3(a=data1,b=data2,c=data3,d=data4,e=data5,f=data6,g=data7,h=data8,i=data9,j=data10,k=data11,l=data12,m=data13,n=data14,o=data15,p=data16,q=data17,username=data18,city=data19,pred=pred,category=category)
        after3.save()
    return render(request,'after3.html', {'data':pred})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password is not same')
            return redirect('register')
    else:
        return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    heart=forms.objects.filter(username=request.user.username)
    liver=forms2.objects.filter(username=request.user.username)
    chronic=forms3.objects.filter(username=request.user.username)    
    # heart=forms.objects.all()
    # liver=forms.objects.all()
    # chronic=forms.objects.all()

    return render(request,"profile.html",{'heart':heart,'liver':liver,'chronic':chronic})

def services(request):
    return render(request,'services.html')