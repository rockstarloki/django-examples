from django.shortcuts import render

def show(request):
    return render(request,"login.html")

def validate(request):
    username = request.POST.get("t1")
    password  = request.POST.get("t2")

    if username == "rockstar" and password == "lokesh":
        return render(request,"Welcome.html",{"user":username})
    else :
        return render(request,"login.html",{"status":"InValid"})

