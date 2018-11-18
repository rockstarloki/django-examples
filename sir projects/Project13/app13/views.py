from django.shortcuts import render


def showIndex(request):
    return render(request,"index.html")


def showImages(request):
    name = request.POST.get("b1")
    return render(request,"show.html",{"iname":name})