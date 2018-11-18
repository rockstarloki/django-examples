from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def welcome(request):
        username = request.POST.get("t1")
        password = request.POST.get("t2")
        if username == "admin" and password == "admin":
            return render(request, "welcome.html", {"who":"admiin"})
        elif username == "ravi" and password == "kumar":
            return render(request, "welcome.html", {"who": "Employee"})
        elif username == "mohan" and password == "krishna":
            return render(request, "welcome.html", {"who": "Employee"})
        elif username == "user1" and password == "one":
            return render(request, "welcome.html", {"who": 'User'})
        elif username == "user2" and password == "two":
            return render(request, "welcome.html", {"who": 'User' })
        else:
            return render(request, "login.html", {"status": "InValid"})

