from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'toodo/home.html')
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'toodo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:  
                return render(request, 'toodo/signupuser.html',{'form':UserCreationForm(),'error':'Username Taken'})
        else:
            return render(request, 'toodo/signupuser.html',{'form':UserCreationForm(),'error':'passwords did not match'})
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'toodo/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
           return render(request, 'toodo/loginuser.html',{'form':AuthenticationForm(),'error':'Username and pasasword didnot match'})
        else:
            login(request, user)
            return redirect('currenttodos')
@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'toodo/currenttodos.html',{'todos':todos})
@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
@login_required
def createtodo(request):
    if request.method == "GET":
        return render(request, 'toodo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'toodo/createtodo.html', {'form':TodoForm(),'error':'Error in data input'})
@login_required
def viewtodo(request, pk):
    todos = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "GET":
        form = TodoForm(instance=todos)
        return render(request, 'toodo/viewtodo.html',{'todos':todos,'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todos)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'toodo/createtodo.html', {'todos':todos,'form':form,'error':'Error in data input'})
@login_required
def complete(request, pk):
    todos = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todos.datecompleted = timezone.now()
        todos.save()
        return redirect('currenttodos')
@login_required
def uncomplete(request, pk):
    todos = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todos.datecompleted = None
        todos.save()
        return redirect('currenttodos')
@login_required
def delete(request, pk):
    todos = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todos.delete()
        return redirect('currenttodos')
@login_required
def completedtodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'toodo/currenttodos.html',{'todos':todos,'completed':True})
 