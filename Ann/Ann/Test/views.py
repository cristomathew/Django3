from django.shortcuts import render, redirect, get_object_or_404
from .forms import TestForm,QForm,ResultForm
from Questions.models import Questions
from .models import Test
from result.models import Result
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import random
qs = []
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def test(request):
    if request.method == "GET":
        tests = Test.objects.all()
        return render(request, 'pages/newtest.html', {'form':TestForm(),'tests':tests})
    else:
        try:
            form = TestForm(request.POST)
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('index')
        except ValueError:
            return render(request, 'pages/newtest.html', {'form':TestForm(),'error':'Error in data input'})
@login_required
def testlist(request):
    if request.method == "GET":
        tests = Test.objects.all()
        return render(request, 'pages/testlist.html', {'form':TestForm(),'tests':tests})
@login_required
def viewtest(request, pk):
    todos = get_object_or_404(Test, pk=pk)
    results = Result.objects.filter(user=request.user,test_name=todos.name)
    res = ResultForm()
    qsa = Questions.objects.filter(topic=todos.topic)
    total = int(todos.urans)
    while len(qs)<total:
        a = random.choice(qsa)
        if a in qs:
            continue
        else:
            qs.append(a)
    if request.method == "GET":
        return render(request, 'pages/viewtest.html',{'todos':todos,'qs':qs,'results':results,'time':todos.time,'range':range(total)})
    else:
        try:
            form = []
            qu=[]
            mlist = []
            count = 0
            totalm = 0
            marks = 0
            for i in qs:
                form.append(request.POST.get(str(i.id)))
            for q in qs:
                qu.append(q.correct)
                mlist.append(q.marks)
            for i in range(total):
                if form[i] == qu[i]:
                    count += 1
                    marks += mlist[i]
                    totalm +=  mlist[i]
                else:
                    totalm +=  mlist[i]
            todos.marks = count
            todos.datecompleted = timezone.now()
            todos.student = request.user.username
            todos.save()
            result = res.save(commit=False)
            result.marks = marks
            result.totalmarks = totalm
            result.user = request.user
            result.test_name = todos.name
            if(marks>total%40):
                result.grade="P"
            else:
                result.grade="F"
            result.save()
            return redirect('index')
        except ValueError:
            return render(request, 'pages/viewtest.html', {'todos':todos,'qs':qs,'count':count,'error':'Error in data input'})
