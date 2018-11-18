from django.shortcuts import render
from .models import MyProduct


# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def saveProduct(request):
    n = request.POST.get("t1")
    na = request.POST.get("t2")
    pri = request.POST.get("t3")

    my = MyProduct(no=n,name=na,price=pri)
    my.save()

    return render(request,"index.html")