from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'pages/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'pages/signupuser.html',{'form':UserCreationForm(),'error':'Username Taken'})
        else:
            return render(request, 'pages/signupuser.html',{'form':UserCreationForm(),'error':'passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'pages/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
           return render(request, 'pages/loginuser.html',{'form':AuthenticationForm(),'error':'Username and pasasword didnot match'})
        else:
            login(request, user)
            return redirect('index')
@login_required
def logoutuser(request):
    logout(request)
    return redirect('index')