from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"index.html")


def displayone(request):
    messsage = request.POST.get("language")
    if messsage == "select":
        mes = "please select one language"
        return render(request,"index.html",{"mess":mes})
    else:
        return render(request,"index.html",{"mess1":messsage})


def displayTwo(request):
    messsage1 = request.POST.get("language")
    return render(request, "index.html", {"mess1": messsage1})
