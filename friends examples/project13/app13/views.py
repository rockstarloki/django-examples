from django.shortcuts import render
from .models import Employee
# Create your views here.
def showLogin(request):
    return render(request,"login.html")


def showRegister(request):
    return render(request,"register.html")


def saveDetails(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    contact=request.POST.get('contact')
    salary=request.POST.get('salary')
    username=request.POST.get('username')
    password=request.POST.get('password')
    emp=Employee(name=name,idno=idno,contact=contact,salary=salary,username=username,password=password)
    emp.save()
    return render(request,"register.html",{"status":"Registerd successfully"})


def loginCheck(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    vc=Employee.objects.filter(username=username,password=password)
    if vc:
        g=Employee.objects.get(username=username)
        return render(request,"hme.html",{"data":g})
    else:
        return render(request,"login.html",{"status":"Invalid username and password"})
    return render(request,"login.html")


def view(request):
    username=request.GET.get('un')
    g=Employee.objects.get(username=username)
    return render(request,"hme.html",{"data":g,"mess":"view"})


def updateProfile(request):
    username = request.GET.get('un')
    g = Employee.objects.get(username=username)
    return render(request, "hme.html", {"data": g, "mess": "update"})


def updateDetails(request):
    idno = request.POST.get('idno')
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    salary = request.POST.get('salary')
    username = request.POST.get('username')
    my=Employee.objects.get(username=username)
    my.name=name
    my.contact=contact
    my.salary=salary
    my.save()
    g = Employee.objects.get(username=username)
    return render(request,"hme.html",{"data": g, "mess": "view","status":"DATA UPDATED"})


def deleteProfile(request):
    username = request.GET.get('un')
    g = Employee.objects.get(username=username)
    return render(request,"hme.html",{"data": g,"dp":g})


def deleteproduct(request):
    opt=request.POST.get('dp')
    if opt=="yes":
        username=request.POST.get('username')
        Employee.objects.filter(username=username).delete()
        return render(request,"login.html",{"status":'EMployee '+username+ 'deleted succefully'})
    else:
        return render(request,"login.html")


def logOut(request):
    return render(request,"login.html")