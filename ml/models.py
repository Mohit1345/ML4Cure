from time import timezone
from django.db import models
import pickle
import numpy as np
from django.contrib.auth.models import User,auth

#admin admin
# Create your models here.
# class user(models.Model):
#     username = models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     password2=models.CharField(max_length=100)
#     def __str__(self):
#         return self.username


class forms(models.Model):
    a=models.IntegerField(max_length=120,default=0)
    b=models.IntegerField(max_length=120,default=0)
    c=models.IntegerField(max_length=120,default=0)
    d=models.IntegerField(max_length=120,default=0)
    e=models.IntegerField(max_length=120,default=0)
    f=models.IntegerField(max_length=120,default=0)
    g=models.IntegerField(max_length=120,default=0)
    h=models.IntegerField(max_length=120,default=0)
    i=models.IntegerField(max_length=120,default=0)
    j=models.IntegerField(max_length=120,default=0)
    k=models.IntegerField(max_length=120,default=0)
    l=models.IntegerField(max_length=120,default=0)
    m=models.IntegerField(max_length=120,default=0)
    n=models.IntegerField(max_length=120,default=0)
    username=models.CharField(max_length=200,default=User.username)
    city=models.CharField(max_length=200,default="pune")
    pred=models.IntegerField(max_length=2,default=0)
    category=models.CharField(max_length=100,default='heart')
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    # dob=models.DateField(_(""), auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.username

class forms2(models.Model):
    a=models.IntegerField(max_length=120,default=0)
    b=models.IntegerField(max_length=120,default=0)
    c=models.IntegerField(max_length=120,default=0)
    d=models.IntegerField(max_length=120,default=0)
    e=models.IntegerField(max_length=120,default=0)
    f=models.IntegerField(max_length=120,default=0)
    g=models.IntegerField(max_length=120,default=0)
    h=models.IntegerField(max_length=120,default=0)
    i=models.IntegerField(max_length=120,default=0)
    j=models.IntegerField(max_length=120,default=0)
    username=models.CharField(max_length=200,default="unknown")
    city=models.CharField(max_length=200,default="pu")
    pred=models.IntegerField(max_length=2,default=0)
    category=models.CharField(max_length=100,default='liver')
    def __str__(self):
        return self.username

class forms3(models.Model):
    a=models.IntegerField(max_length=120,default=0)
    b=models.IntegerField(max_length=120,default=0)
    c=models.IntegerField(max_length=120,default=0)
    d=models.IntegerField(max_length=120,default=0)
    e=models.IntegerField(max_length=120,default=0)
    f=models.IntegerField(max_length=120,default=0)
    g=models.IntegerField(max_length=120,default=0)
    h=models.IntegerField(max_length=120,default=0)
    i=models.IntegerField(max_length=120,default=0)
    j=models.IntegerField(max_length=120,default=0)
    k=models.IntegerField(max_length=120,default=0)
    l=models.IntegerField(max_length=120,default=0)
    m=models.IntegerField(max_length=120,default=0)
    n=models.IntegerField(max_length=120,default=0)
    o=models.IntegerField(max_length=120,default=0)
    p=models.IntegerField(max_length=120,default=0)
    q=models.IntegerField(max_length=120,default=0)
    username=models.CharField(max_length=200,default="unknown")
    city=models.CharField(max_length=200,default="pu")
    pred=models.IntegerField(max_length=2,default=0)
    category=models.CharField(max_length=100,default='heart')
    # dob=models.DateField(_(""), auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.username


# class User(models.Model):
#     username=models.CharField(max_length=120)
#     password=models.CharField(max_length=120)
#     email=models.EmailField(max_length=120)
#     contact=models.IntegerField(max_length=10)
#     dob=models.DateField(max_length=211)
#     city=models.CharField(max_length=132)



