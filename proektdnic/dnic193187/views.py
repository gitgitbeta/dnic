from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tests, Question

# Create your views here.
from .models import Lectures


def home(request):
    return render(request,"auth/index.html")
def h(request):
    return render(request,"auth/index.html")
def l1(request):
    queryset = Lectures.objects.all()[:1].filter()
    context = {"l1": queryset}
    return render(request,"auth/l1.html",context=context)
def l2(request):
    queryset = Lectures.objects.all()[1:2].filter()
    context = {"l2": queryset}
    return render(request,"auth/l2.html",context=context)
def l3(request):
    queryset = Lectures.objects.all()[2:3].filter()
    context = {"l3": queryset}
    return render(request,"auth/l3.html",context=context)
def l4(request):
    queryset = Lectures.objects.all()[3:4].filter()
    context = {"l4": queryset}
    return render(request,"auth/l4.html",context=context)
def l5(request):
    queryset = Lectures.objects.all()[4:5].filter()
    context = {"l5": queryset}
    return render(request,"auth/l5.html",context=context)

def lectures(request):
    return render(request,"auth/lectures.html")

def t1(request):
    queryset = Question.objects.all().filter(test=1)
    context = {"t1": queryset}
    return render(request,"auth/t1.html",context=context)
def t2(request):
    queryset = Question.objects.all().filter(test="test2")
    context = {"t2": queryset}
    return render(request,"auth/t2.html",context=context)
def t3(request):
    queryset = Question.objects.all().filter(test="test3")
    context = {"t3": queryset}
    return render(request,"auth/t3.html",context=context)
def t4(request):
    queryset = Question.objects.all().filter(test="test4")
    context = {"t4": queryset}
    return render(request,"auth/t4.html",context=context)
def t5(request):
    queryset = Question.objects.all().filter(test="test5")
    context = {"t5": queryset}
    return render(request,"auth/t5.html",context=context)

def test(request):
    return render(request,"auth/test.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "your acc is created")
        return redirect('signin')
    return render(request,"auth/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request,"auth/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad credentials")
            return redirect('home')

    return render(request,"auth/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"loged out sucessfuly")
    return redirect('home')

