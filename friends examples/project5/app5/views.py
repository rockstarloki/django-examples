from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request,"index.html")

def validate(request):

    username=request.POST.get("username")
    password=request.POST.get("pass")

    if  username == "sathya" and password == "tech":

        return render(request,"index.html",{"mess":"valid"})


    else:
        return render(request,"index.html",{"mess":"invalid"})


