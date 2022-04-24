import email
from email import message
import imp
from os import stat
from django.db import connection
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.views import View
from pytz import timezone
# Create your views here.
from .models import email_user, User, emai_l, schedule_task
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.utils import timezone

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Home(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect("PROFILE")

        return render(request, 'home.html')

    def post(self, request):

        pass


class Login(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect("PROFILE")

        return render(request, 'login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        try:
            connection = authenticate(username=username, password=password)
        except:
            connection = False

        if (connection):
            
            login(request, connection)
            return redirect("PROFILE")
        
        else:
            
            message = True
            
            data = {
                'message': message,
            }

            return render(request, 'login.html', data)


class Logout(View):

    def get(self, request):

        logout(request)
        return redirect('LOGIN')

class Register(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect("PROFILE")

        return render(request, 'register.html')

    def post(self, request):

        username    = request.POST['username']
        email_adr   = request.POST['email']
        password    = request.POST['password']
        

        try: 
            itexist = User.objects.get(username=username)
        except:
            itexist = False


        if(itexist):

            message = 'Username Already exists'

            data = {
                'message': message,
            }

            return render(request, 'register.html', data)

        else:

            user    = User.objects.create_user(username, email=email_adr, password=password)
            e_user  = email_user.objects.create(e_user=user, username=username, password=password, email_adr=email_adr)

            created = True
            data = {
                'created': created,
            }

            return render(request, 'register.html', data)


class Profile(View):

    def get(self, request):
        
        scheduled_emails = schedule_task.objects.filter(to__username=request.user, sent=False)

        for email in scheduled_emails:
            
            if email.date_time <= timezone.now():
                
                emai_l.objects.create(r_user=email.to, subject=email.subject, from_adr=email.your_addr, date_time=email.date_time, content=email.content, attachment=email.attachment)                

                
                # instance of MIMEMultipart
                msg = MIMEMultipart()
                
                # storing the senders email address  
                msg['From'] = email.your_addr
                
                # storing the receivers email address 
                msg['To'] = email.to.email_adr
                
                # storing the subject 
                msg['Subject'] = email.subject
                
                # string to store the body of the mail
                body = email.content
                
                print(email.your_addr)
                # attach the body with the msg instance
                #msg.attach(MIMEText(body, 'plain'))
                
                # open the file to be sent 
                #filename = "File_name_with_extension"
                #attachment = open("Path of the file", "rb")
                
                # instance of MIMEBase and named as p
                #p = MIMEBase('application', 'octet-stream')
                
                # To change the payload into encoded form
                #p.set_payload((attachment).read())
                
                # encode into base64
                #encoders.encode_base64(p)
                
                #p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                
                # attach the instance 'p' to instance 'msg'
                #msg.attach(p)
                
                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(email.your_addr, email.email_password)
                #text = msg.as_string()
                s.sendmail(email.your_addr, email.to.email_adr, email.content)
                s.quit()

                
                email.sent      = True
                email.save()


        email_list = emai_l.objects.filter(r_user__username=request.user)

        

        return render(request, 'profile.html', {'email_list': email_list})

    def post(self, request):

        if 'email_id' in request.POST:

            id = request.POST['email_id']
            email = emai_l.objects.get(id=id)
            email.delete()
        
            

            return redirect("PROFILE")

        status          = request.POST.get('read')
        
        if status == None:
            status = False
            id              = request.POST['email_status']
            email           = emai_l.objects.get(id=id)
            email.read      = status
            email.save()         


        if 'read' in request.POST:

            status          = request.POST['read']

            if status == 'on':
                status = True

            id              = request.POST['email_status']
            email           = emai_l.objects.get(id=id)
            email.read      = status
            email.save()            

        return redirect("PROFILE")
    


