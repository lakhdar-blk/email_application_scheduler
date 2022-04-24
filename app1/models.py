from asyncio.windows_events import NULL
from asyncore import read
from datetime import date
import email
import imp
from importlib.resources import contents
from operator import mod
from django.db import models

from django.contrib.auth.models import User
import datetime


class email_user(models.Model):

    e_user      = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    username    = models.CharField(max_length=255, unique=True)
    password    = models.CharField(max_length=255)
    email_adr   = models.EmailField(max_length=255, default=NULL)  

    def __str__(self):
        return self.username

class emai_l(models.Model):

    r_user      = models.ForeignKey(email_user,on_delete=models.CASCADE)
    subject     = models.CharField(max_length=255)
    from_adr    = models.EmailField(max_length=255)
    date_time   = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    content     = models.TextField()
    attachment  = models.FileField(upload_to='uploads/')
    read        = models.BooleanField(default=False)

    def __str__(self):
        return "Mail for "+str(self.r_user)

class schedule_task(models.Model):

    to              = models.ForeignKey(email_user,on_delete=models.CASCADE)
    subject         = models.CharField(max_length=255)
    your_addr       = models.EmailField(max_length=255)
    email_password  = models.CharField(max_length=255)
    date_time       = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    content         = models.TextField()
    attachment      = models.FileField(upload_to='uploads/')
    sent            = models.BooleanField(default=False)