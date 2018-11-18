from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def display(request):
    mess = request.POST.get("rb")
    return render(request,"index.html",{"message":mess})