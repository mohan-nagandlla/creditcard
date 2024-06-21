from tkinter import CASCADE

from django.db import models

# Create your models here.
from User.models import UserTransaction_Model


class Sendquery(models.Model):
    transid=models.ForeignKey(UserTransaction_Model,on_delete=CASCADE)
    sendquery=models.CharField(max_length=400)
    name=models.CharField(max_length=100)