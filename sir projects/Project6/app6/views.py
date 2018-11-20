from django.shortcuts import render

# Create your views here.
def showLogin(request):
    return render(request,"login.html")


def validate(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")
    if username == "sathya" and  password == "tech":
        return render(request,"welcome.html",{"user":username})
    else:
        return render(request,"login.html",{"status":"Invalid"})