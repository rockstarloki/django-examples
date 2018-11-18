from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def validate(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")
    if username == "admin" and password == "admin":
        return render(request,"admin.html",{"who":username})
    elif username == "ravi" and password == "kumar":
        return render(request,"employee.html",{"who":username})
    elif username == "mohan" and password == "krishna":
        return render(request,"employee.html",{"who":username})
    elif username == "user1" and password == "one":
        return render(request,"user.html",{"who":username})
    elif username == "user2" and password == "two":
        return render(request,"user.html",{"who":username})
    else :
        return render(request,"login.html",{"status":"InValid"})

