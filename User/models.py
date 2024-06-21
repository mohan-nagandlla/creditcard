from tkinter import CASCADE

from django.db import models

# Create your models here.



class UserRegister_Model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    phoneno = models.IntegerField()
    gender = models.CharField(max_length=10)

class UserAccount_Model(models.Model):
    uuname = models.ForeignKey(UserRegister_Model,on_delete=CASCADE)
    cardholder = models.CharField(max_length=50)
    carttype = models.CharField(max_length=50)
    issuingbank = models.CharField(max_length=50)
    cardnumber = models.IntegerField()
    cvv = models.IntegerField()
    issusedate = models.DateField()
    expiredate = models.DateField()
    pinnumber= models.IntegerField()
    creditlimit = models.IntegerField()

class UserTransaction_Model(models.Model):
    tname = models.ForeignKey(UserRegister_Model, on_delete=CASCADE)
    tcarttype = models.CharField(max_length=50)
    tcardnumber = models.IntegerField()
    tccv = models.IntegerField()
    texpiredate = models.DateField()
    tpinnumber = models.IntegerField()
    tamount = models.IntegerField()
    tdate = models.DateField()
    ttime = models.TimeField()


class UserComplaint_Model(models.Model):
    cuname = models.ForeignKey(UserRegister_Model, on_delete=CASCADE)
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    accountnumber = models.IntegerField()
    username = models.CharField(max_length=50)
    mobilenumber = models.IntegerField()
    complaint = models.TextField()
    date = models.DateField()
    time = models.TimeField()

