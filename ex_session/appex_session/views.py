from django.shortcuts import render
from .models import Commentdetails

def Showindex(request):
    value = request.session("username")
    if value == "":
        return render(request,"comment.html")
    else:
        return render(request,"index.html",{"message":"comment is alredy given"})

def index(request):
    return render(request,"index.html")

def comment(request):
    name = request.POST.get("t1")
    contact = request.POST.get("t2")
    comnt = request.POST.get("t3")

    cd = Commentdetails(name=name,contact=contact,comment=comnt)
    cd.save()

    request.session["username"] = name

    return render(request,"index.html",{"mess":"comment saved"})

