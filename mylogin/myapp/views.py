from django.shortcuts import render

def login(request):
    return render(request,"index.html")
def validate(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    if username == "rockstar" and password == "lokesh":
        return render(request,"imag.html", {"message": "valid"})
    else:
        return render(request,"index.html",{"message":"Invalid"})
