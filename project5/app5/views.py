from django.shortcuts import render

def showlogin(request):
    return render(request,"login.html")

def loginvalidation(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    if  un == "rockstar" and pa == "lokesh":
        print("valid")
    else:
        print("Invalid")
    return render(request, "login.html")
