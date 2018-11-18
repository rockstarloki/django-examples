from django.shortcuts import render
from .models import CommentDetails



def showIndex(request):
    return render(request,"index.html")

def comment(request):

    value = request.session["username"]
    if value == "":
        return render(request, "comment.html")
    else:
        return render(request, "index.html",{"mes":"Comment is Given"})


def commentRegister(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    message = request.POST.get("t3")

    cd = CommentDetails(name=name,contact=cno,message=message)
    cd.save()

    request.session["username"] = name

    return render(request,"index.html",{"mes":"Comment is Saved"})
