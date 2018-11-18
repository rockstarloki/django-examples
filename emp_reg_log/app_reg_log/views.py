from django.shortcuts import render
from .models import Emp
# Create your views here.

def home(request):
    return render(request,"login.html")

def login(request):
    uname  = request.POST.get("username")
    upass = request.POST.get("password")

    res = Emp.objects.filter(username=uname,password=upass)
    if res:
        print("valid")
        pas = Emp.objects.get(username=uname)
        return render(request,"welcome.html",{"pass":pas})
    else:
        print("Invalid")
        return render(request,"login.html",{"message":"Invalid"})

def Register(request):
    return render(request,"register.html")

def Registered(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    email =  request.POST.get("email")
    username = request.POST.get("username")
    passsword  =request.POST.get("password")

    s = Emp(idno=idno,name=name,contact=contact,salary=salary,email=email,username=username,password=passsword)
    s.save()

    return render(request,"register.html",{"message":"Employee registered successfully"})


def Viewprofile(request):
    uname =request.GET.get("uname")
    pas = Emp.objects.get(username=uname)
    return render(request,"welcome.html",{"profile":pas,"pass":pas})


def Updateprofile(request):
    uname = request.GET.get("uname")
    pas = Emp.objects.get(username=uname)
    return render(request, "welcome.html", {"update":pas,"pass": pas})

def Logout(request):
    return render(request,"login.html")


def UpdateProfile(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    email = request.POST.get("email")
    username = request.POST.get("username")
    passsword = request.POST.get("password")

    s = Emp(idno=idno, name=name, contact=contact, salary=salary, email=email, username=username, password=passsword)
    s.save()

    return render(request,"welcome.html",{"mess":s})


def Deleteprofile(request):
    uname = request.GET.get("uname")
    pas = Emp.objects.get(username=uname)
    return render(request, "welcome.html", {"delete":pas,"pass": pas})


def DeleteProfile(request):
    uname = request.POST.get("uname")
    res = request.POST.get("rd")
    if res == "Yes":
        Emp.objects.get(username=uname).delete()
        return render(request,"login.html")
    else:
        return render(request,"welcome.html")
