from django.shortcuts import render, redirect, get_object_or_404
from .models import Result
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
@login_required
def resultlist(request):
    if request.method == "GET":
        results = Result.objects.filter(user=request.user)
        return render(request, 'pages/result.html', {'results':results})
@login_required
def resultview(request, pk):
    result = get_object_or_404(Result, pk=pk)
    user = request.user
    if request.method == "GET":
        return render(request, 'pages/viewResult.html',{'result':result,'user':user})
    