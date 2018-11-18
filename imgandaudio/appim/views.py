from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def show(request):
     name = request.POST.get("t1")
     if name == "rockstar" or name == "lokesh" or name == "stylishstar" or name == "mybike" or name == "guitar" :
         return render(request,"show.html",{"name":name})
     else:
         return render(request,"j.html", {"name": "Not Available"})
