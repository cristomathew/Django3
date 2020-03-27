from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('strength') == 'weak':
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('strength') == 'avg':
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        characters.extend('1234567890')
    if request.GET.get('strength') == 'strong':
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        characters.extend('+!@#$%^&*')
    length = int(request.GET.get('length'))
    thepass = ''
    for x in range(length):
        thepass += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepass})