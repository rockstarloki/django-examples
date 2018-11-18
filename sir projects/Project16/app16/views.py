from django.shortcuts import render, redirect
from .models import UserRegister

def showIndex(request):
    return render(request,"index.html")

def showRegister(request):
    return render(request,"register.html")

def showLogin(request):
    return render(request,"login.html")

def registerUser(request):
    name = request.POST.get("r_name")
    age = request.POST.get("r_age")
    contact = request.POST.get("r_cno")
    email = request.POST.get("r_email")
    password = request.POST.get("r_password")

    ur = UserRegister(contact=contact,name=name,age=age,email=email,password=password)
    ur.save()

    res = redirect("/index/")
    return res
    #return render(request,"login.html")

def loginUser(request):
    em = request.POST.get("l_email")
    pa = request.POST.get("l_password")

    qs = UserRegister.objects.filter(email=em,password=pa)
    print(qs)

    if qs.count() == 0:
        return render(request, "login.html",{"mess":"Invalid"})
    else:
        return render(request, "home.html",{"l_email":em})

