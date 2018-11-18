from django.shortcuts import render
from .models import Employee
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showRegister(request):
    return render(request,"register.html")


def saveDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    username = request.POST.get("username")
    password = request.POST.get("password")

    e = Employee(idno=idno,name=name,contact=contact,salary=salary,username=username,password=password)
    e.save()

    return render(request,"register.html",{"message":"Employee Registred"})


def loginCheck(request):
    uname = request.POST.get("username")
    upass = request.POST.get("password")

    res = Employee.objects.filter(username=uname,password=upass)

    if res:
        print("Valid")
        res = Employee.objects.get(username=uname)

        return render(request,"welcome.html",{"emp":res})
    else:
        print("In-Valid")
        return render(request, "index.html",{"message":"Invalid User"})


def viewProfile(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request,"welcome.html",{"profile":res,"emp":res})


def deleteProfile(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request,"welcome.html",{"delete":res,"emp":res})


def delete(request):
    option = request.POST.get("a")
    username = request.POST.get("uname")

    if option == "Yes":
        Employee.objects.filter(username=username).delete()
        return render(request, "index.html")
    else:
        return render(request,"index.html")


def updateprofile(request):
    username = request.GET.get("uname")
    res = Employee.objects.get(username=username)
    return render(request, "welcome.html", {"update": res, "emp": res})

def updateDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    salary = request.POST.get("salary")
    username = request.POST.get("username")
    password = request.POST.get("password")

    e = Employee(idno=idno,name=name,contact=contact,salary=salary,username=username,password=password)
    e.save()

    return render(request, "welcome.html", {"profile": e, "emp": e})
