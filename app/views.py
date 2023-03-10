from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def login(req):
      if req.method == 'POST': 
            username = req.POST['unP']
            password = req.POST['pwP']
            logStudent = auth.authenticate(username=username, password=password)
            if logStudent is None:
                  return redirect('login')
            else:
                  return redirect('form')
      return render(req, 'login.html')
      
def register(req):
      if req.method == 'POST': 
            username = req.POST['unR']
            password = req.POST['pwR']
            email = req.POST['email']
            regStudent = User.objects.create_user(username=username, password=password, email=email)
            regStudent.save()
            print("User Registered Successfully.")
      return render(req,'register.html')      

def form(req):
      return render(req, 'form.html')