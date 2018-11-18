from django.shortcuts import render
from  .models import Employee

def Index(request):
    return render(request,"index.html")

def OpenRegister(request):
    return render(request,"registration.html")

def Register(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    username = request.POST.get("username")
    password = request.POST.get("password")
    res = Employee(idno=idno, name=name, contact=contact, salary=salary, username=username, password=password)
    res.save()
    return render(request, "registration.html", {"mess": "Employee registered"})

def Login(request):
    return render(request, "login.html")

def OpenLogin(request):
    uname = request.POST.get("username")
    upass = request.POST.get("password")

    res = Employee.objects.filter(username=uname, password=upass)
    if res:
        print("Valid")
        res = Employee.objects.get(username=uname)
        return render(request,"welcome.html", {"message":res})
    else:
        print("Invalid")
        return render(request,"login.html", {"msg": "invalid"})


def ViewProfile(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request,"welcome.html",{"profile":res,"message":res})


def DeleteProfile(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request,"welcome.html",{"delete":res,"message":res})


def DeleteProfile1(request):
    name=request.POST.get('uname')
    opt=request.POST.get('rd')
    if opt=="Yes":
        Employee.objects.filter(username=name).delete()
        return  render(request,"login.html")
    else:
        return render(request,"login.html")


def Logout(request):
    return render(request,"login.html",)


def Update(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request,"welcome.html",{"update": res,"message":res})


def UpdateDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    username = request.POST.get("username")
    password = request.POST.get("password")
    res = Employee(idno=idno, name=name, contact=contact, salary=salary, username=username, password=password)
    res.save()

    return render(request, "welcome.html",{"profile":res, "message": res})


