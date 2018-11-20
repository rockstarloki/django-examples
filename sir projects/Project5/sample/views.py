from django.shortcuts import render

def showLogin(request):
    return render(request,"login_page.html")


def loginValidation(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    if un == "sathya" and pa == "tech":
        print("Valid")
    else :
        print("Invalid")
    return render(request,"login_page.html")