from django.shortcuts import render
from .models import Comment

def index(request):
    return render(request,"index.html",{"mess": "already given"})

def message(request):
    return render(request,"comment.html",)

def showIndex(request):
    name = request.POST.get("t1")
    contact = request.POST.get("t2")
    comment = request.POST.get("t3")

    cm = Comment(name=name,contact=contact,comment=comment)
    cm.save()
    request.session["username"] = name

    return render(request,"comment.html")
