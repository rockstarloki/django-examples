from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def validation(request):
    uname = request.POST.get("username")
    upass = request.POST.get("pass")
    if uname == "sathya" and upass == "tech":
        message = "Valid"
    else:
        message = "Invalid"
    return render(request,"index.html",{"mess":message})